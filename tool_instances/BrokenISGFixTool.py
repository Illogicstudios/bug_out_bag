from tool_models.ActionTool import *


class BrokenISGFixTool(ActionTool):
    def _action(self):
        lockNode('initialShadingGroup', lock=0, lockUnpublished=0)
        lockNode('initialParticleSE', lock=0, lockUnpublished=0)

    def __init__(self):
        super().__init__(name="Broken ISG fixer",pref_name="broken_isg_fixer",
                         description="Fix broken initialShadingGroup", button_text="Fix",
                         tooltip="Fix the initialShadingGroup")