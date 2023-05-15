import json
import sys
import re

def rewrite_invoke2call(arg_str):
    return arg_str.replace("invoke", "call")
    
def rewrite(*args):
    for p in args:
        # read in
        with open(p, "r") as f:
            raw_str = f.read()
            # back up
            with open(f"{p}.bak", "w") as g:
                g.write(raw_str)
        
        # rewrite
        new_str = rewrite_invoke2call(raw_str)

        # write back
        with open(p, "w") as f:
            f.write(new_str)


if __name__ == "__main__":

    if(len(sys.argv) < 1):
        print("Usage: rewriter.py [ll files]")
        sys.exit(1)

    rewrite(*sys.argv[1:])
