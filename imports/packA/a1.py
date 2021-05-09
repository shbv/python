a1_x = 1
def a1_func():
    print("a1_func")

""" Explicit relative imports """
""" Uses relative path from current module:
        from .<module/package> import X     (. = curr dir ;  .. = 1 dir up ;  ... = 2 dirs up ; etc)
        .. can only go upto project root dir i.e. script dir
    Note:
    1. We are running "python imports.py" (located one level up, so that dir is in sys.path)
    2. We cannot run "python a1.py" anymore if relative imports exist as in this script
       If we want to run "a1.py" as script, 
            a. From root directory, run it as module "python -m packA.a1". 
               But if packA has __init__.py with "from a1 import *", it'll run a1 twice
            b. Add root directory into sys.path in this module & use all absolute imports from the root folder. Shown below in commented section.
               Also we cannot have "if __name__ == '__main__'" section with relative imports in the file.
               Only then we can run "python a1.py"
    Bottomline: Using relative imports => makes running scripts under the package directly harder.
"""

"""
# Only needed for Note 2b, i.e. if we want to run "python a1.py"
import os, sys
root_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
print(f"Adding {root_path} to sys.path")
sys.path.append(root_path)
print(f"sys.path: {sys.path}")
import temp             # relatively at ../temp.py. This is absolute import since dir is in sys.path & no . is used
from packA import a2        # relatively at ./
from packA.subA import sa1   # relatively at ./sa1.py
"""
import temp             # relatively at ../temp.py. This is absolute import since dir is in sys.path & no . is used
from . import a2        # relatively at ./
from .subA import sa1   # relatively at ./sa1.py


""" Implicit relative imports"""
""" Not supported from Python 3"""  
# import temp
# import a2
# import subA.sa1

# Debug message
print("Running packA/a1.py")

# Run only if "python -m a1", or "python a1.py". Not when its imported
if __name__ == "__main__":
    print("Running main section in packA/a1.py")
