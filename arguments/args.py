""" 
Run: 
python args.py -v1 "xyz"
python args.py -v1 "xyz" -v2 10 -v3 1.1 -v4 True
python args.py -v1 "xyz" -v2 10 -v3 1.1 -v4 True -v5 100
"""

import sys
import argparse


""" Using sys """
def print_sys_args():
    print("== args using sys: ==")
    for ix, arg in enumerate(sys.argv): 
        print(f"arg{ix}: {arg}")
    print()
    
""" Using argparse - recommended way"""
def get_args():
    
    parser = argparse.ArgumentParser(
            description = "This code is an example for argparse usage",
            epilog = "\
            Examples: \
                python args.py -v1 \"xyz\"; \
                python args.py -v1 \"xyz\" -v2 10 -v3 1.1 -v4; \
                python args.py -v1 \"xyz\" -v2 10 -v3 1.1 -v4 -v5 100\
            ")
    parser.add_argument('-v1', '--var1', type=str, default="", help='description of var1', required=True)
    parser.add_argument('-v2', '--var2', type=int, default=0, help='description of var2')
    parser.add_argument('-v3', '--var3', type=float, default=0.0, help='description of var3')
    parser.add_argument('-v4', '--var4', default=True, action='store_false', help='description of var4') # -v4 => set it to False
    parser.add_argument('-v5', '--var5', type=int, default=argparse.SUPPRESS, help='description of var5') # no default value
    
    print("== args help using argparse: ==")
    parser.print_help()
    print()
    
    print("== args using argparse: ==")
    args = parser.parse_args()  
    print(f"args: {args}")

    return args

""" Main function """
if __name__ == "__main__":
    print_sys_args()
    opts = get_args()
    print(f"opts: {opts}")  # Namespace
    print(f"opts.var1: {opts.var1}")
    print(f"vars(opts): {vars(opts)}") # Dictionary (returns opts.__dict__ or locals() )
    for opt in vars(opts).items():
        print(opt)
    
