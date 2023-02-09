from BobTool import *


class ActionTool(BobTool, ABC):
    def __init__(self, name, pref_name, description, button_text="Run"):
        super().__init__(name, pref_name)
        self.__description = description
        self.__button_text = button_text

    @abstractmethod
    def _action(self):
        pass

    def populate(self):
        layout = super().populate()
        # Get the collapsible widget (the only widget of the layout)
        collapsible = layout.itemAt(0).widget()
        content_layout = QHBoxLayout(collapsible.contentWidget)
        content_layout.setContentsMargins(5, 5, 5, 5)
        # Add a button and assign the action button to its clicked event
        hlyt = QHBoxLayout()
        content_layout.addLayout(hlyt)

        desc_lbl = QLabel(self.__description)
        desc_lbl.setWordWrap(True)
        hlyt.addWidget(desc_lbl, 1)

        action_btn = QPushButton(self.__button_text)
        action_btn.clicked.connect(self._action)
        hlyt.addWidget(action_btn)
        return layout