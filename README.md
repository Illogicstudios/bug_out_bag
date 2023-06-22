# Bug-out Bag (BOB)

Bob is toolbox gathering many others tools.

## How to install

You will need some files that several Illogic tools need. You can get them via this link :
https://github.com/Illogicstudios/common

---

## How to use

Hover the tools to know how to use them

---

## How to add new tools

To create a new tool, follow these steps : 
- Copy one of the templates stored in `/tool_instances/templates/` into the `/tool_instances/` folder with the name you like
- Go into the `/BobApp.py` file to add this new tool. In the constructor you can add a BobCategory or adding the tool to an existing one.
```python
    # Model attributes
    self.__bob_categories = [
        # BobCategory([...]),
        BobCategory("NameCategory", self.__prefs, [
          YourTool()
        ]),
        # BobCategory([...])
    ]
```
You also have to import the tool
```python
from .tool_instances.YourTool import *
```
- Add to the tool what you want it to do. Take inspiration from tools that have already been created. You can also have a look at the tool models in `/tool_models/` to know all the posssible parameters and functions.
