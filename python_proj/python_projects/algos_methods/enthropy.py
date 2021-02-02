# import math
import numpy as np

def entropy(p1,p2):
    return -p1*np.log2(p1) - p2*np.log2(p2)

print(entropy((3/4),(1/4)),entropy((1/4),(3/4)))
print(entropy((1/1),(0)), entropy((5/9),(4/9)))
print(entropy((5/5),(0/5)), entropy((1/5),(4/5)))
print(entropy((0/4),(4/4)), entropy((6/6),(0/6)))
# print(entropy((1/5),(4/5)), entropy((1/5),(4/5)))
