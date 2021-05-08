"""
Reference: 
    https://chrisyeh96.github.io/2017/08/08/definitive-guide-python-imports.html#appendix-list-of-always-built-in-modules
Terms:
    built-in module = module compiled into Python interpreter
    module          = any <module>.py file 
    package         = any <module> folder (if Python version < 3.3: needs __init__.py, even if its empty)   
    object          = funcs,classes,vars
Syntax/Behavior:
    import <module>/<package> 
    from <package> import <module>/<subpackage>/<object>
    from <module> import <object>
        => All objects (funcs,classes,vars) in <module/package> available to importer
        import <module> => all code in <module>.py is run
        import <package> => all code in <package>/__init__.py is run (i.e. __init__.py is imported as module)
        Searches sys.path search path for <module>.py or <module> folder. 
            sys.path order = built-in-modules from standard library, 
                             current script directory, 
                             standard library path (from PYTHONPATH variable or default sys.path locations)
            E.g.: If math.py, random.py in current dir:  
                import math => from standard library (not current dir), 
                import random => from current dir
            [x[1] for x in pkgutil.iter_modules(path=None)]  => List all modules in sys.path
            [x[1] for x in pkgutil.iter_modules(path=['.'])] => List all modules in current script directory
    Note: 
    1. "python <modulefile>.py" in <module> folder does not call <module> folder's __init_.py since its not considered a package anymore
    2. "pip install -e <project>"  adds <project> directory to sys.path making it a importable package => import <project>
Object referencing:
    import X  / from Y import X
    X = module/package  => objects in X are referenced as X.object (<module>.object or <package>.<module>.object)
    X = object          => referenced as object
"""

""" Regular imports"""
# import <module>/<package>
# import <module>/<package> as <aliasname>
import os, sys 
print(os.getcwd())
print(sys.path)
import urllib.error # submodule
import numpy as np
print(np.zeros(2))
import pkgutil
print("Accesible names in package sys:", dir(pkgutil))
print("First 10 modules in sys.path:", [x[1] for x in pkgutil.iter_modules(path=None)][:10])
print("First 10 modules in script dir:", [x[1] for x in pkgutil.iter_modules(path=['.'])][:10])

""" Regular imports using 'from' """
# from <package> import <module>/<subpackage>/<object>
# from <module> import <object>
from time import *
from os import path, walk, remove
print(time)
print(path.curdir)

""" Regular absolute imports (preferred over relative imports)"""
""" Uses full path from script root folder"""
#from packA import a1   # Does not need __init__.py 
#import packA.a1        # Does not need __init__.py
import packA            # Needs __init__.py with objects to be accessible. Not useful without __init__.py.
packA.a1.a1_func()      # Needs __init__.py: Normal call to module object in package
packA.a1_func()         # Needs __init__.py: Flexible call due to import a1_func() in package __init__.py 
print(packA.a1.a1_x)
print(packA.a1_x)
# Full path: <package>.<subpackage>.<module>.<object>
import packA.subA.sa1
packA.subA.sa1.helloWorld()
# Just function <object>
from packA.subA.sa1 import helloWorld
helloWorld()
# Middle ground <module>.<object>
import packA.subA.sa1 as sa1
sa1.helloWorld()

""" Explicit relative imports"""
# See packA/a1.py

""" Implicit relative imports"""
# See packA/a1.py


