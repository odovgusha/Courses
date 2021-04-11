import sys
#print(s.find("ab"))
setup = list()
for line in sys.stdin:
    # start_time = time.time()
    setup.append(line.replace('\n',''))
    #print(list(map(str, (line.split()))))



#setup = list(setup)
#print(setup)
s,t = setup




def num_of_reps(s,t):
    k = 0
    num_rep = 0
    while s[k:].find(t) != -1:
        #print(k)
        k = s[k:].find(t)+k
        k+=1
        num_rep += 1
    return num_rep

print(num_of_reps(s,t))