#!/usr/bin/python

import sys
import json
import os

print ('Number of arguments:', len(sys.argv), 'arguments.')
#print ('Argument List:', str(sys.argv))
#print([arg for arg in sys.argv])
print(sys.argv[1])

"""
for file in os.listdir("/mydir"):
    if file.endswith(".txt"):
        print(os.path.join("/mydir", file))
"""
