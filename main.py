import os
import pcbnew
from .ui_impl import frmMainImpl
import builtins
import gettext
tr = gettext.translation('zone_manager', os.path.join(os.path.dirname(__file__), 'lang'),
                         languages=['zh_CN'])
tr.install('zone_manager')


class AreaManagerPlugin(pcbnew.ActionPlugin):
    def defaults(self):
        self.name = _("Area Manager")
        self.category = _("Modify PCB")
        self.description = _("Manage priority of many copper areas")
        self.show_toolbar_button = True

    def Run(self):
        m_mainWin = frmMainImpl(None)

        m_mainWin.Exec(pcbnew.GetBoard())
