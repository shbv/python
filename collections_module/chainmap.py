"""
Returns first value from multiple keys
Useful for overriding variables

Run:
    python chainmap.py
    python chainmap.py --uid 'cmd_line_user' --passwd 'cmd_line_pass'
"""

import argparse
import os
from collections import ChainMap

def parse_args():

    parser = argparse.ArgumentParser()
    parser.add_argument('--uid', type=str, default=argparse.SUPPRESS)
    parser.add_argument('--passwd', type=str, default=argparse.SUPPRESS)
    args = parser.parse_args()
    cmd_line_args = vars(args)
    print(f"cmd_line_args: {cmd_line_args}")
    
    defaults = {'uid': 'default_user', 'passwd': 'default_pass'}
    print(f"defaults: {defaults}")

    # order of preference: cmd line, env setting, defaults
    chain = ChainMap(cmd_line_args, os.environ, defaults)
    return chain

if __name__ == '__main__':

    print("== no env setting ==")
    opts = parse_args()
    print(f"opts['uid']: {opts['uid']}, opts['passwd']: {opts['passwd']}")
    print()

    print("== with env setting ==")
    os.environ['uid'], os.environ['passwd'] = 'env_user', 'env_pass'
    print(f"os.environ['uid']: {os.environ['uid']}, os.environ['passwd']: {os.environ['passwd']}")
    opts = parse_args()
    print(f"opts['uid']: {opts['uid']}, opts['passwd']: {opts['passwd']}")
    print()


