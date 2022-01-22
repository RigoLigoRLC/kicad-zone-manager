import pcbnew
from .ui_impl import frmMainImpl


class AreaManagerPlugin(pcbnew.ActionPlugin):
    def defaults(self):
        self.name = "Area Manager"
        self.category = "Modify PCB"
        self.description = "Manage priority of many copper areas"
        self.show_toolbar_button = True

    def Run(self):
        m_mainWin = frmMainImpl(None)

        m_mainWin.Exec(pcbnew.GetBoard())
