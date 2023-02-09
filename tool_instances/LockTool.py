from tool_models.MultipleActionTool import *

from pymel.core import *


class LockTool(MultipleActionTool):

    def __init__(self):
        actions = {
            "lock": {
                "text": "Lock transform",
                "action": self.__lock_selection
            },
            "unlock": {
                "text": "Unlock transform",
                "action": self.__unlock_selection
            }
        }
        super().__init__(name="Lock",pref_name="lock_tool", actions=actions, stretch=True)
        self.__select_children = True
        self.__ignore_root = False
        self.__select_children_checkbox = None
        self.__ignore_root_checkbox = None

    def populate(self):
        layout = super(LockTool, self).populate()
        self.__refresh_btn()
        return layout

    def __get_transforms_selected(self):
        selection = ls(selection=True, type="transform")
        if self.__ignore_root:
            transforms = []
        else:
            transforms = selection
        if self.__select_children:
            for sel in selection:
                transforms.extend(listRelatives(sel, allDescendents=True, type="transform"))
        return transforms

    def __lock_selection(self):
        selection = self.__get_transforms_selected()
        for transform in selection:
            transform.translate.lock()
            transform.rotate.lock()
            transform.scale.lock()
        self.__refresh_btn()

    def __unlock_selection(self):
        selection = self.__get_transforms_selected()
        for transform in selection:
            transform.translate.unlock()
            transform.translateX.unlock()
            transform.translateY.unlock()
            transform.translateZ.unlock()
            transform.rotate.unlock()
            transform.rotateX.unlock()
            transform.rotateY.unlock()
            transform.rotateZ.unlock()
            transform.scale.unlock()
            transform.scaleX.unlock()
            transform.scaleY.unlock()
            transform.scaleZ.unlock()
        self.__refresh_btn()

    def __refresh_btn(self):
        selection = self.__get_transforms_selected()
        unlocked = False
        locked = False
        for transform in selection:
            t_locked = transform.translate.isLocked()
            tx_locked = transform.translateX.isLocked()
            ty_locked = transform.translateY.isLocked()
            tz_locked = transform.translateZ.isLocked()
            r_locked = transform.rotate.isLocked()
            rx_locked = transform.rotateX.isLocked()
            ry_locked = transform.rotateY.isLocked()
            rz_locked = transform.rotateZ.isLocked()
            s_locked = transform.scale.isLocked()
            sx_locked = transform.scaleX.isLocked()
            sy_locked = transform.scaleY.isLocked()
            sz_locked = transform.scaleZ.isLocked()
            unlocked |= t_locked or tx_locked or ty_locked or tz_locked or \
                        r_locked or rx_locked or ry_locked or rz_locked or \
                        s_locked or sx_locked or sy_locked or sz_locked
            locked |= not t_locked or not tx_locked or not ty_locked or not tz_locked or \
                        not r_locked or not rx_locked or not ry_locked or not rz_locked or \
                        not s_locked or not sx_locked or not sy_locked or not sz_locked
            if locked and unlocked: break
        self._actions["lock"]["button"].setEnabled(locked)
        self._actions["unlock"]["button"].setEnabled(unlocked)

    def on_selection_changed(self):
        self.__refresh_btn()

    def on_dag_changed(self):
        self.__refresh_btn()

    def on_select_children_state_changed(self, state):
        self.__select_children = state == 2
        self.__refresh_btn()

    def on_ignore_root_state_changed(self, state):
        self.__ignore_root = state == 2
        self.__refresh_btn()

    def _add_in_ui(self, lyt):
        cb_lyt = QHBoxLayout()
        cb_lyt.setAlignment(Qt.AlignCenter)
        lyt.addLayout(cb_lyt)
        self.__select_children_checkbox = QCheckBox("Select children")
        self.__select_children_checkbox.stateChanged.connect(self.on_select_children_state_changed)
        self.__select_children_checkbox.setChecked(self.__select_children)
        cb_lyt.addWidget(self.__select_children_checkbox)
        self.__ignore_root_checkbox = QCheckBox("Ignore root")
        self.__ignore_root_checkbox.stateChanged.connect(self.on_ignore_root_state_changed)
        self.__ignore_root_checkbox.setChecked(self.__ignore_root)
        cb_lyt.addWidget(self.__ignore_root_checkbox)


