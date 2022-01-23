import os
import pcbnew
from .ui_impl import frmMainImpl
import builtins
import gettext
result=gettext.bindtextdomain('zone_manager', os.path.join(os.path.dirname(__file__), 'lang'))
gettext.textdomain('zone_manager')
builtins.__dict__['_'] = gettext.gettext

for i in result:
    print(i)

class AreaManagerPlugin(pcbnew.ActionPlugin):
    def defaults(self):
        self.name = "Area Manager"
        self.category = "Modify PCB"
        self.description = "Manage priority of many copper areas"
        self.show_toolbar_button = True

    def Run(self):
        m_mainWin = frmMainImpl(None)

        m_mainWin.Exec(pcbnew.GetBoard())
