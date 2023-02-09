import sys

if __name__ == '__main__':
    # TODO specify the right path
    install_dir = 'PATH/TO/bug_out_bag'
    if not sys.path.__contains__(install_dir):
        sys.path.append(install_dir)

    modules = [
        "BobApp",
        "Prefs",
        "BobElement",
        "BobCategory",
        "BobTool",
        "BobCollapsibleWidget",
        # Tool Models
        "tool_models.ActionTool",
        "tool_models.MultipleActionTool",
        "tool_models.RoutineTool",
        # Tool Instance Templates
        "tool_instances.ActionTemplateTool",
        "tool_instances.MultipleActionTemplateTool",
        "tool_instances.RoutineTemplateTool",
        # Tool Instances
        "tool_instances.LockTool",
    ]

    from utils import *
    unload_packages(silent=True, packages=modules)

    for module in modules:
        importlib.import_module(module)

    from BobApp import *
    app = BobApp()
    app.show()