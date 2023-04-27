import importlib
from common import utils

utils.unload_packages(silent=True, package="bug_out_bag")
importlib.import_module("bug_out_bag")
from bug_out_bag.BobApp import BobApp
try:
    bob.close()
except:
    pass
bob = BobApp()
bob.show()
