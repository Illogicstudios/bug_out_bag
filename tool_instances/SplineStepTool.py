from tool_models.MultipleActionTool import *


class SplineStepTool(MultipleActionTool):
    def __init__(self):
        actions = {
            "to_linear_step": {
                "text": "In To Linear and Out to Stepped",
                "action": self.__to_linear_step,
                "stretch": 5,
            },
            "to_legacy": {
                "text": "To Auto (Legacy)",
                "action": self.__to_legacy,
                "stretch": 3,
            },
        }
        super().__init__(name="Spline Step", pref_name="spline_step_tool",
                         actions=actions)

    def __to_linear_step(self):
        keyTangent(g=True, inTangentType="linear")
        keyTangent(g=True, outTangentType="step")
        self.__refresh_btn()

    def __to_legacy(self):
        keyTangent(g=True, inTangentType="auto")
        keyTangent(g=True, outTangentType="auto")
        self.__refresh_btn()

    def __refresh_btn(self):
        in_tangent, out_tangent, weighted_tangent = keyTangent(g=True, query=True)
        linear_stepped_enabled = in_tangent != "linear" or out_tangent != "step"
        legacy_enabled = in_tangent != "auto" or out_tangent != "auto"
        if "button" in self._actions["to_linear_step"]:
            self._actions["to_linear_step"]["button"].setEnabled(linear_stepped_enabled)
        if "button" in self._actions["to_legacy"]:
            self._actions["to_legacy"]["button"].setEnabled(legacy_enabled)

    def populate(self):
        layout = super(SplineStepTool, self).populate()
        self.__refresh_btn()
        return layout
