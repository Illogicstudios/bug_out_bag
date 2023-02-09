from tool_models.RoutineTool import *


class RoutineTemplateTool(RoutineTool):

    def __init__(self):
        steps = {
                "Step 1":{
                    "action": self.__action_1
                },
                "Step 2": {
                    "action": self.__action_2
                },
                "Step 3": {
                    "action": self.__action_3,
                    "checked" : False
                }
            }
        super().__init__(name="Routine Template Tool", pref_name="routine_template_tool",
                         steps=steps,button_text="Run", step_checked_default = True)

    def __action_1(self):
        print("Step 1")

    def __action_2(self):
        print("Step 2")

    def __action_3(self):
        print("Step 3")