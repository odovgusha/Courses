import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    print(re.sub(r"\b[aA]+\b","argh",line,count=1))

    
    # process line