import os
import sys

from functools import partial

from pymel.core import *
import maya.OpenMayaUI as omui
import maya.OpenMaya as OpenMaya

from PySide2 import QtCore
from PySide2 import QtGui
from PySide2 import QtWidgets
from PySide2.QtWidgets import *
from PySide2.QtCore import *

from shiboken2 import wrapInstance

import utils

from Prefs import *
from BobCategory import *

# from tool_instances.RoutineTemplateTool import *
# from tool_instances.ActionTemplateTool import *
# from tool_instances.MultipleActionTemplateTool import *
from tool_instances.LockTool import *

# ######################################################################################################################

_FILE_NAME_PREFS = "bug_out_bag"

_BOB_TOOLS = [
    BobCategory("Transform", [
        LockTool(),
    ]),
]

# ######################################################################################################################


class BobApp(QDialog):

    def __init__(self, prnt=wrapInstance(int(omui.MQtUtil.mainWindow()), QWidget)):
        super(BobApp, self).__init__(prnt)

        # Common Preferences (common preferences on all illogic tools)
        self.__common_prefs = Prefs()
        # Preferences for this tool
        self.__prefs = Prefs(_FILE_NAME_PREFS)

        # Model attributes
        self.__bob_categories = _BOB_TOOLS

        # Assign Prefs to categories
        for categ in self.__bob_categories:
            categ.set_prefs(self.__prefs)

        # UI attributes
        self.__ui_width = 400
        self.__ui_height = 500
        self.__ui_min_width = 300
        self.__ui_min_height = 350
        self.__tab_widget = None

        # name the window
        self.setWindowTitle("Bug-out bag")
        # make the window a "tool" in Maya's eyes so that it stays on top when you click off
        self.setWindowFlags(QtCore.Qt.Tool)
        # Makes the object get deleted from memory, not just hidden, when it is closed.
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

        self.__create_callback()

        # Create the layout, linking it to actions and refresh the display
        self.__create_ui()
        self.__refresh_ui()

    # Create callbacks when DAG changes and the selection changes
    def __create_callback(self):
        self.__selection_callback = \
            OpenMaya.MEventMessage.addEventCallback("SelectionChanged", self.__on_selection_changed)
        self.__dag_callback = \
            OpenMaya.MEventMessage.addEventCallback("DagObjectCreated", self.__on_dag_changed)

    # Remove callbacks
    def closeEvent(self, arg__1: QtGui.QCloseEvent) -> None:
        OpenMaya.MMessage.removeCallback(self.__selection_callback)
        OpenMaya.MMessage.removeCallback(self.__dag_callback)

    # Create the ui
    def __create_ui(self):
        # Reinit attributes of the UI
        self.setMinimumSize(self.__ui_min_width, self.__ui_min_height)
        self.resize(self.__ui_width, self.__ui_height)
        self.move(QDesktopWidget().availableGeometry().center() - self.frameGeometry().center())

        # asset_path = os.path.dirname(__file__) + "/assets/asset.png"

        # Main Layout
        main_lyt = QVBoxLayout()
        main_lyt.setContentsMargins(5, 8, 5, 8)
        self.setLayout(main_lyt)
        self.__tab_widget = QTabWidget()
        main_lyt.addWidget(self.__tab_widget)

    # Refresh the ui according to the model attribute
    def __refresh_ui(self):
        self.__tab_widget.clear()
        for bob_categ in self.__bob_categories:
            bob_categ_lyt = bob_categ.populate()
            # bob_categ_widget = QWidget()
            # bob_categ_widget.setLayout(bob_categ_lyt)
            self.__tab_widget.addTab(bob_categ_lyt, bob_categ.get_name())

    def __on_selection_changed(self, *args, **kwargs):
        for bob_categ in self.__bob_categories:
            bob_categ.on_selection_changed()

    def __on_dag_changed(self, *args, **kwargs):
        for bob_categ in self.__bob_categories:
            bob_categ.on_dag_changed()
