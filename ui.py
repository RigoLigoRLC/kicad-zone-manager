# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

import gettext
_ = gettext.gettext

###########################################################################
## Class frmMain
###########################################################################

class frmMain ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"Zone Manager"), pos = wx.DefaultPosition, size = wx.Size( 337,380 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		sizerMain = wx.BoxSizer( wx.HORIZONTAL )

		self.nbkMain = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		sizerMain.Add( self.nbkMain, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( sizerMain )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class pnlCopperZone
###########################################################################

class pnlCopperZone ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 324,341 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		sizerCopperMain = wx.BoxSizer( wx.VERTICAL )

		sizerCopperSplit = wx.BoxSizer( wx.HORIZONTAL )

		self.treeCopperZone = wx.TreeCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE|wx.TR_FULL_ROW_HIGHLIGHT|wx.TR_HIDE_ROOT|wx.TR_MULTIPLE|wx.TR_NO_LINES )
		sizerCopperSplit.Add( self.treeCopperZone, 2, wx.EXPAND, 5 )

		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		self.btnCopperPrioUp = wx.Button( self, wx.ID_ANY, _(u"^"), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.btnCopperPrioUp, 0, wx.TOP|wx.RIGHT|wx.LEFT, 5 )

		self.btnCopperPrioDown = wx.Button( self, wx.ID_ANY, _(u"v"), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.btnCopperPrioDown, 0, wx.RIGHT|wx.LEFT, 5 )

		self.btnCopperRemove = wx.Button( self, wx.ID_ANY, _(u"X"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btnCopperRemove.Hide()

		bSizer6.Add( self.btnCopperRemove, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )

		self.lblDirectlySet = wx.StaticText( self, wx.ID_ANY, _(u"Set all to"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblDirectlySet.Wrap( -1 )

		bSizer6.Add( self.lblDirectlySet, 0, wx.TOP|wx.RIGHT|wx.LEFT, 5 )

		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

		self.txtDirectlySet = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 55,-1 ), 0 )
		bSizer5.Add( self.txtDirectlySet, 0, wx.FIXED_MINSIZE|wx.BOTTOM|wx.LEFT, 5 )

		self.btnSetTo = wx.Button( self, wx.ID_ANY, _(u">"), wx.DefaultPosition, wx.Size( 20,-1 ), 0 )
		bSizer5.Add( self.btnSetTo, 0, wx.BOTTOM|wx.RIGHT, 5 )


		bSizer6.Add( bSizer5, 1, wx.EXPAND, 5 )


		bSizer6.Add( ( 0, 0), 10, wx.EXPAND, 5 )

		self.btnOk = wx.Button( self, wx.ID_ANY, _(u"OK"), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.btnOk, 0, wx.TOP|wx.RIGHT|wx.LEFT, 5 )

		self.btnCancel = wx.Button( self, wx.ID_ANY, _(u"Cancel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.btnCancel, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )

		self.btnInspect = wx.Button( self, wx.ID_ANY, _(u"inspect"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btnInspect.Hide()

		bSizer6.Add( self.btnInspect, 0, wx.ALL, 5 )


		sizerCopperSplit.Add( bSizer6, 0, 0, 5 )


		sizerCopperMain.Add( sizerCopperSplit, 1, wx.EXPAND, 5 )


		self.SetSizer( sizerCopperMain )
		self.Layout()

		# Connect Events
		self.treeCopperZone.Bind( wx.EVT_TREE_ITEM_COLLAPSING, self.treeCopperZoneOnTreeItemCollapsing )
		self.treeCopperZone.Bind( wx.EVT_TREE_SEL_CHANGED, self.treeCopperZoneOnTreeSelChanged )
		self.treeCopperZone.Bind( wx.EVT_TREE_SEL_CHANGING, self.treeCopperZoneOnTreeSelChanging )
		self.btnCopperPrioUp.Bind( wx.EVT_BUTTON, self.btnCopperPrioUpOnButtonClick )
		self.btnCopperPrioDown.Bind( wx.EVT_BUTTON, self.btnCopperPrioDownOnButtonClick )
		self.btnCopperRemove.Bind( wx.EVT_BUTTON, self.btnCopperRemoveOnButtonClick )
		self.btnSetTo.Bind( wx.EVT_BUTTON, self.btnSetToOnButtonClick )
		self.btnOk.Bind( wx.EVT_BUTTON, self.btnOkOnButtonClick )
		self.btnCancel.Bind( wx.EVT_BUTTON, self.btnCancelOnButtonClick )
		self.btnInspect.Bind( wx.EVT_BUTTON, self.InspectOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def treeCopperZoneOnTreeItemCollapsing( self, event ):
		event.Skip()

	def treeCopperZoneOnTreeSelChanged( self, event ):
		event.Skip()

	def treeCopperZoneOnTreeSelChanging( self, event ):
		event.Skip()

	def btnCopperPrioUpOnButtonClick( self, event ):
		event.Skip()

	def btnCopperPrioDownOnButtonClick( self, event ):
		event.Skip()

	def btnCopperRemoveOnButtonClick( self, event ):
		event.Skip()

	def btnSetToOnButtonClick( self, event ):
		event.Skip()

	def btnOkOnButtonClick( self, event ):
		event.Skip()

	def btnCancelOnButtonClick( self, event ):
		event.Skip()

	def InspectOnButtonClick( self, event ):
		event.Skip()


