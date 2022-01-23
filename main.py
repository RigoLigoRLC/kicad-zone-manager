import os
import pcbnew
from .ui_impl import frmMainImpl
import gettext
gettext.bindtextdomain('zone_manager', os.path.join(os.path.dirname(__file__), 'lang'))
gettext.textdomain('zone_manager')
os.environ['LC_MESSAGES'] = __import__('locale').getdefaultlocale()[0]
__import__('builtins').__dict__['_'] = gettext.gettext

class AreaManagerPlugin(pcbnew.ActionPlugin):
    def defaults(self):
        self.name = _("Area Manager")
        self.category = _("Modify PCB")
        self.description = _("Manage priority of many copper areas")
        self.show_toolbar_button = True
        self.icon_file_name = os.path.join(os.path.dirname(__file__), 'icon.png')

    def Run(self):
        m_mainWin = frmMainImpl(None)

        m_mainWin.Exec(pcbnew.GetBoard())
