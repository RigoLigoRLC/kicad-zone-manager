from .ui import *
import pcbnew
import platform
import builtins
builtins.__dict__['_'] = wx.GetTranslation


isWin = platform.system() == "Windows"
internalCopper = pcbnew.LSET_InternalCuMask().CuStack()


def pGetFancyLayerName(layer: pcbnew.LSET):
    ret = ''
    cu = layer.CuStack()
    if pcbnew.F_Cu in cu:
        ret += 'F/'
    if pcbnew.B_Cu in cu:
        ret += 'B/'
    for i in internalCopper:
        if i in cu:
            ret += str(i) + '/'
    return ret.removesuffix('/')


class pnlCopperZoneImpl(pnlCopperZone):
    m_rootNodeId = None
    m_prioToZone = {}  # This and the next dict should always maintains one-to-one correspondence to the UI Nodes,
    m_prioToNode = {}  # as well as after a cleanup cycle
    m_transaction = {}

    def __init__(self, parent):
        super(pnlCopperZoneImpl, self).__init__(parent)
        # wx.MessageBox("hello")

    def pGetAllItems(self):
        ret = []
        tree = self.treeCopperZone
        lvl = tree.GetFirstChild(self.m_rootNodeId)[0]
        while lvl.IsOk():
            item = tree.GetFirstChild(lvl)[0]
            while item.IsOk():
                ret.append(item)
                item = tree.GetNextSibling(item)
            lvl = tree.GetNextSibling(lvl)
        return ret

    def pAddZoneToPriorityLevel(self, priority, area):
        # wx.MessageBox(area.GetZoneName(), area.GetNetname())
        if priority not in self.m_prioToZone:
            self.m_prioToZone[priority] = [area]
        else:
            self.m_prioToZone[priority].append(area)

    # pAddZoneToUiTree IMPLIES pAddZoneToPriorityLevel !!
    def pAddZoneToUiTree(self, priority, area, tree: wx.TreeCtrl, text) -> wx.TreeItemId:
        ret = None
        keys = list(self.m_prioToNode.keys())
        keys.sort(reverse=True)
        if priority not in keys:
            # Creation of new Priority node, needs to determine the position to make the tree correct
            insertPos = 0
            # If desired priority is higher than all others, then create it at top
            if keys[0] < priority:
                insertPos = 0
            # If desired priority is lower than all others, then create it at bottom
            elif keys[-1] > priority:
                insertPos = -1
            # Then, search in the PrioToNode Mapping to find the first priority larger than the desired priority
            else:
                i = 0
                while keys[i] > priority:  # Search smallest
                    i = i + 1
                insertPos = i
            # print('{}'.format(insertPos))
            base = tree.InsertItem(self.m_rootNodeId, insertPos, _(u'Priority %d') % priority, -1, -1, priority)
            ret = tree.AppendItem(base,
                                  text,
                                  -1, -1,
                                  (priority, area))
            self.m_prioToNode[priority] = base
            tree.Expand(base)
        else:
            ret = tree.AppendItem(self.m_prioToNode[priority],
                                  text,
                                  -1, -1,
                                  (priority, area))
        self.pAddZoneToPriorityLevel(priority, area)
        return ret

    def pChangeZonePriorityTo(self, tree: wx.TreeCtrl, item, zone, prev, dest, addSelect: bool):
        new = self.pAddZoneToUiTree(dest, zone, tree, tree.GetItemText(item))  # Add to new priority
        self.m_prioToZone[prev].remove(zone)  # Delete from original priority
        self.m_transaction[zone] = dest  # Add operation to transaction list
        tree.Delete(item)  # Delete from original position in UI
        if isWin:  # FIXME Windows has problem dealing with reselect behavior
            tree.UnselectAll()
        else:
            if addSelect:
                tree.SelectItem(new)  # Make new item selected

    def pIncreaseItemPriority(self, tree: wx.TreeCtrl, item, addSelect: bool):
        data = tree.GetItemData(item)
        self.pChangeZonePriorityTo(tree, item, data[1], data[0], data[0] + 1, addSelect)

    def pDecreaseItemPriority(self, tree: wx.TreeCtrl, item, addSelect: bool):
        data = tree.GetItemData(item)
        self.pChangeZonePriorityTo(tree, item, data[1], data[0], data[0] - 1, addSelect)

    def pIncreaseSelectionPriority(self):
        tree = self.treeCopperZone
        for i in tree.GetSelections():
            self.pIncreaseItemPriority(tree, i, True)
        self.pCleanupAfterPriorityChange()

    def pDecreaseSelectionPriority(self):
        tree = self.treeCopperZone
        sel = tree.GetSelections()
        # If we're moving a group already with a 0 priority zone, then we should shift everyone else up instead
        othersUp = False
        for i in reversed(sel):
            if tree.GetItemData(i)[0] == 0:
                othersUp = True
                break
        if othersUp:
            for i in [x for x in self.pGetAllItems() if x not in sel]:
                print(tree.GetItemText(i))
                self.pIncreaseItemPriority(tree, i, False)
        # Otherwise we just do normal decreasing
        else:
            for i in sel:
                self.pDecreaseItemPriority(tree, i, True)
        self.pCleanupAfterPriorityChange()

    def pCleanupAfterPriorityChange(self):
        for i in list(self.m_prioToZone.keys()):
            if len(self.m_prioToZone[i]) == 0:  # Found an empty priority level, purge all associated items
                self.treeCopperZone.Delete(self.m_prioToNode[i])
                self.m_prioToZone.pop(i)
                self.m_prioToNode.pop(i)

    def Exec(self, board: pcbnew.BOARD):
        zones = board.Zones()

        # Initialize internal data
        self.m_prioToZone = {}

        for i in pcbnew.ZONES(zones):
            if not i.IsOnCopperLayer():
                continue
            if not i.GetIsRuleArea():
                self.pAddZoneToPriorityLevel(i.GetPriority(), i)
            else:
                pass

        # Add to UI
        tree = self.treeCopperZone
        treeRoot = tree.AddRoot('root_dummy')
        self.m_rootNodeId = treeRoot
        keys = list(self.m_prioToZone.keys())
        keys.sort(reverse=True)
        for prio in keys:
            # wx.MessageBox(str(prio))
            lvlItem = tree.AppendItem(treeRoot, _(u'Priority %d') % prio, -1, -1, prio)
            self.m_prioToNode[prio] = lvlItem
            for area in self.m_prioToZone[prio]:
                # wx.MessageBox(area.GetZoneName(), area.GetNetname)
                tree.AppendItem(lvlItem,
                                u'{0}[{1}] @ {2}'.format(area.GetZoneName(),
                                                         area.GetNetname(),
                                                         pGetFancyLayerName(
                                                             area.GetLayerSet())),
                                -1, -1,
                                (prio, area))
        tree.ExpandAll()

        self.Show()

        pass

    # ##### EVENT HANDLERS #####

    def btnCopperPrioDownOnButtonClick(self, event):
        self.pDecreaseSelectionPriority()

    def btnCopperPrioUpOnButtonClick(self, event):
        self.pIncreaseSelectionPriority()

    def treeCopperZoneOnTreeSelChanging(self, event):
        tree = self.treeCopperZone
        item = event.GetItem()
        if tree.GetItemParent(item) == self.m_rootNodeId:
            event.Veto()
            tree.SelectChildren(item)

    def treeCopperZoneOnTreeSelChanged(self, event):
        tree = self.treeCopperZone
        for i in tree.GetSelections():
            if tree.GetItemParent(i) == self.m_rootNodeId:  # Discard incorrectly selected nodes
                tree.UnselectItem(i)  # FIXME Doesn't work, will always select the full group of OldItem. Not sure why

    def treeCopperZoneOnTreeItemCollapsing(self, event):
        event.Veto()

    def InspectOnButtonClick(self, event):
        ret = ''
        # for i in self.m_transaction:
        #     ret += ('{}, {}\n'.format(str(i[0]), str(i[1])))
        for i in self.m_prioToNode.keys():
            ret += str(i) + ', '
        wx.MessageBox(ret)

    def btnOkOnButtonClick(self, event):
        for i in self.m_transaction:
            i.SetPriority(self.m_transaction[i])
        self.m_transaction.clear()
        self.GetParent().GetParent().EndModal(wx.ID_OK)

    def btnCancelOnButtonClick(self, event):
        self.m_transaction.clear()
        self.GetParent().GetParent().EndModal(wx.ID_CANCEL)

    def btnSetToOnButtonClick(self, event):
        dest = 0
        try:
            dest = int(self.txtDirectlySet.GetValue())
            assert (dest >= 0)
        except:
            self.txtDirectlySet.Clear()
            return
        tree = self.treeCopperZone
        for i in tree.GetSelections():
            data = tree.GetItemData(i)
            self.pChangeZonePriorityTo(tree, i, data[1], data[0], dest, True)
        self.pCleanupAfterPriorityChange()



class frmMainImpl(frmMain):

    def __init__(self, parent):
        super(frmMainImpl, self).__init__(parent)
        self.m_pgCopperZone = pnlCopperZoneImpl(self.nbkMain)
        self.nbkMain.AddPage(self.m_pgCopperZone, _(u'Copper Zones'), True)

    def Exec(self, board: pcbnew.BOARD):
        self.m_pgCopperZone.Exec(board)
        self.ShowModal()
