import sys
#print(s.find("ab"))
setup = list()
for line in sys.stdin:
    # start_time = time.time()
    setup.append(line.replace('\n',''))
    #print(list(map(str, (line.split()))))



#setup = list(setup)
#print(setup)
s,a,b = setup

def string_sub(s,a,b):
    reps = 0
    if s.find(a) != -1:
        if b.find(a) == -1:
            #print("fine")
            #return(s.replace(a,b))
            while s.find(a) != -1 and reps <= 1000:
                s = s.replace(a,b)
                reps += 1
                
            return reps
        else:
            return ('Impossible')
        
    return reps

print(string_sub(s,a,b))