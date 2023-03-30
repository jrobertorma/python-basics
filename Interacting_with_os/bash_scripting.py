#!/usr/bin/env python3
import sys
import subprocess

with open(sys.argv[1]) as file:
    lines = file.readlines()
    for line in lines:
        oldfilename = line.strip()
        newfilename = oldfilename.replace("jane", "jdoe")
        subprocess.run(["mv", oldfilename, newfilename])
file.close()