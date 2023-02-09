from PySide2 import QtCore
from PySide2 import QtWidgets
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from BobElement import *

from BobCollapsibleWidget import *


class BobTool(BobElement, ABC):
    def __init__(self, name, pref_name):
        super(BobTool, self).__init__(name)
        self.__pref_name = pref_name
        self.__prefs = None

    def populate(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(2,3,2,3)
        collapsible = BobCollapsibleWidget(self._name, self.__pref_name, self.__prefs, bg_color="rgb(50, 50, 50)", widget_color="rgb(93, 93, 93)", margins=[3, 3, 3, 3])
        layout.addWidget(collapsible)
        return layout

    def on_selection_changed(self):
        pass

    def on_dag_changed(self):
        pass

    def set_prefs(self,prefs):
        self.__prefs = prefs