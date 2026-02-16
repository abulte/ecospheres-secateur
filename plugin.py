import os

from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QAction

from .ui.dialog import SecateurDialog


class Plugin:
    def __init__(self, iface):
        self.iface = iface
        self.action = None
        self.dialog = None

    def initGui(self):
        icon_path = os.path.join(os.path.dirname(__file__), "resources", "icon.png")
        icon = QIcon(icon_path) if os.path.exists(icon_path) else QIcon()
        self.action = QAction(icon, "Ecosphères Secateur", self.iface.mainWindow())
        self.action.triggered.connect(self.run)
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu("&Ecosphères Secateur", self.action)

    def unload(self):
        if self.action:
            self.iface.removeToolBarIcon(self.action)
            self.iface.removePluginMenu("Ecosphères Secateur", self.action)
        if self.dialog:
            self.dialog.close()
            self.dialog = None

    def run(self):
        if self.dialog is None:
            self.dialog = SecateurDialog(self.iface)
        self.dialog.show()
        self.dialog.raise_()
        self.dialog.activateWindow()
