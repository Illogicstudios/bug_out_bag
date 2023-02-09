from functools import partial

from BobTool import *


class RoutineTool(BobTool, ABC):
    def __init__(self, name, pref_name, steps, button_text="Run",step_checked_default = True):
        super().__init__(name, pref_name)
        self.__description = "description"
        self.__button_text = button_text

        self.__steps = {}
        for step_name, step in steps.items():
            self.__steps[step_name] = {
                "action": step["action"],
                "checked": step["checked"] if "checked" in step else step_checked_default,
                "checkbox" : None
            }
        self.__run_btn = None
        self.__refreshing = False

    def populate(self):
        layout = super().populate()
        # Get the collapsible widget (the only widget of the layout)
        collapsible = layout.itemAt(0).widget()
        content_layout = QHBoxLayout(collapsible.contentWidget)
        content_layout.setContentsMargins(5, 5, 5, 5)
        # Add a button and assign the action button to its clicked event
        hlyt = QVBoxLayout()
        content_layout.addLayout(hlyt)

        self.__global_cb = QCheckBox()
        self.__global_cb.stateChanged.connect(self.__on_global_state_changed)
        hlyt.addWidget(self.__global_cb)

        for step_name, step in self.__steps.items():
            lyt_step = QHBoxLayout()
            step_cb = QCheckBox()
            step_cb.setChecked(step["checked"])
            self.__steps[step_name]["checkbox"] = step_cb
            step_cb.stateChanged.connect(partial(self.__on_step_state_modified,step_name))
            lyt_step.addWidget(step_cb)
            step_label = QLabel(step_name)
            step_label.setWordWrap(True)
            lyt_step.addWidget(step_label,1)
            hlyt.addLayout(lyt_step)

        self.__run_btn = QPushButton(self.__button_text)
        self.__run_btn.setSizePolicy(QSizePolicy.Minimum,QSizePolicy.Minimum)
        self.__run_btn.clicked.connect(self.__run)
        hlyt.addWidget(self.__run_btn,0,Qt.AlignRight)
        self.__refresh_ui()
        return layout

    def __run(self):
        for step in self.__steps.values():
            if step["checked"]:
                step["action"]()

    def __refresh_ui(self):
        enabled = False
        checked = True
        for step in self.__steps.values():
            if step["checked"]:
                enabled = True
            else:
                checked = False
        self.__refreshing = True
        self.__run_btn.setEnabled(enabled)
        self.__global_cb.setChecked(checked)
        self.__refreshing = False

    def __on_step_state_modified(self, step_key, state):
        self.__steps[step_key]["checked"] = state == 2
        self.__refresh_ui()

    def __on_global_state_changed(self, state):
        if not self.__refreshing:
            for step_name in self.__steps.keys():
                self.__steps[step_name]["checkbox"].setChecked(state == 2)
            self.__refresh_ui()
