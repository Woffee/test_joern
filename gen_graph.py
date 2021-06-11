import pandas as pd
import os
import subprocess
import tempfile

if not os.path.exists("tmp/"):
    os.makedirs("tmp/")

def generate_prolog():

    caller_tree = ""
    short_filename = "caller_and_callee.c"
    with open("tmp/" + short_filename, 'w') as fw:
        with open("test.c", "r") as f:
            fw.write(f.read())

    print(short_filename)
    cmd = "joern-parse tmp/ --out tmp/cpg.bin.zip"
    p = os.popen(cmd)
    x = p.read()
    print(x)

    # subprocess.check_call(["joern-parse ./tmp/ --out ./tmp/cpg.bin.zip"])

    tree = subprocess.check_output(
        "joern --script joern_cfg_to_dot.sc --params cpgFile=tmp/cpg.bin.zip",
        shell=True,
        universal_newlines=True,
    )
    pos = tree.find("digraph g {")
    print(pos)
    if pos >0:
        tree = tree[pos:]
    caller_tree = caller_tree+tree+'\n'+'-'*50+'\n'
    with open("caller_tree.txt", "w") as fw:
        fw.write(caller_tree)


if __name__=="__main__":
    generate_prolog()
