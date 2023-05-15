import json
import sys
import re

def rewrite_invoke2call_expr(arg_list):
    new_list = []
    i = 0
    while i<len(arg_list):
        p = arg_list[i]
        if p.startswith("invoke ") and i<len(arg_list)-1:
            q = arg_list[i+1]
            if q.startswith("to label "):
                # rewrite!
                # FIXME: dump the 'unwind' part
                new_q = q.split(" ")[:3]
                new_q[0] = "br" # replace "to" to "br"
                new_list.append(p.replace("invoke", "call"))
                new_list.append(" ".join(new_q))
                i += 2
            else:
                new_list.append(arg_list[i])
                i += 1
        else:
            new_list.append(arg_list[i])
            i += 1
    return new_list

def rewrite_invoke2call_assign(arg_list):
    new_list = []
    i = 0
    while i<len(arg_list):
        p = arg_list[i]
        plist = p.split(" ")
        if " ".join(plist[1:3])=="= invoke" and i<len(arg_list)-1:
            q = arg_list[i+1]
            if q.startswith("to label "):
                # rewrite!
                # FIXME: dump the 'unwind' part
                new_q = q.split(" ")[:3]
                new_q[0] = "br" # replace "to" to "br"
                new_list.append(p.replace("invoke", "call"))
                new_list.append(" ".join(new_q))
                i += 2
            else:
                new_list.append(arg_list[i])
                i += 1
        else:
            new_list.append(arg_list[i])
            i += 1
    return new_list          
    
def rewrite(*args):
    for p in args:
        # read in
        with open(p, "r") as f:
            raw_str = f.read()
            # back up
            with open(f"{p}.bak", "w") as g:
                g.write(raw_str)
        
        # rewrite
        raw_list = raw_str.split("\n")
        raw_list = [p.strip() for p in raw_list] # remove leading whitespaces
        new_list = rewrite_invoke2call_expr(raw_list)
        new_list = rewrite_invoke2call_assign(new_list)
        new_str = "\n".join(new_list)

        # write back
        with open(p, "w") as f:
            f.write(new_str)


if __name__ == "__main__":

    if(len(sys.argv) < 1):
        print("Usage: rewriter.py [ll files]")
        sys.exit(1)

    rewrite(*sys.argv[1:])
