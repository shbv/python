"""
Context manager protocal:
    with <expression> [as variable]:
        <with code block>
    => <expression> returns an object that supports __enter__() & __exit__() methods
        __enter__()
        <with code block>
        __exit__()
"""

""" file example """
print("== open file ==")
with open('temp.txt', 'r') as fp:   # open file's __enter__() returns file object
    for line in fp:
        print(line)     # __exit__() closes file
print()

""" context manager from scratch """
class Readfile_custom():
    def __init__(self, fname, mode):
        self.fname = fname
        self.mode = mode
        self.fp = None
    def __enter__(self):
        self.fp = open(self.fname, self.mode)
        return self.fp
    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.fp.close()
print("== Readfile_custom using class ==")
with Readfile_custom('temp.txt', 'r') as fp:
    for line in fp:
        print(line)
print()

""" context manager from scratch using contextlib """
import contextlib
@contextlib.contextmanager
def Readfile_context(fname, mode):
    try:
        fp = open(fname, mode)
        yield fp
    except OSError:
        print(f"Found error opening {fname}")
    finally:
        fp.close()
print("== Readfile_custom using contextlib ==")
with Readfile_context('temp.txt', 'r') as fp:
    for line in fp:
        print(line)
print()

""" context manager util: suppress exceptions """
print("== contextlib.suppress ==")
with contextlib.suppress(FileNotFoundError):  
    with open('temp1.txt', 'r') as fp:   
        for line in fp:
            print(line)     
print()

""" context manager util: redirect stdout/stderr """
print("== redirect stdout to file ==")
import sys 
with open('temp1.txt', 'w') as fp:   
    with contextlib.redirect_stdout(fp):
        help(sum)
print()

