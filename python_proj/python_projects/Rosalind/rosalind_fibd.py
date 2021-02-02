f=open("D:/Documents/python_projects/Rosalind/rosalind_fibd.txt", "r")
if f.mode == 'r':
    mode = f.read()
f.close()

r=1
d=int(mode.split()[1])
n=int(mode.split()[0])
# d=4
# n=10

rab_arr = []
total = 0
a=1
b=1
c=0
for x in range(n):
    if x < 2:
        b=1
        # print(x,b)
        rab_arr.append(b)
    elif x >= 2 and x < d:
        c = b
        b = b + a
        a = c
        rab_arr.append(b)
        # print(x,b)
    else:
        i=2
        b=0
        maxpos = len(rab_arr)
        # print(len(rab_arr),"len")
        print(rab_arr)
        # print(rab_arr[-1])
        while i<=(d):

            print(rab_arr[maxpos - i], maxpos, i)
            b += rab_arr[maxpos-i]
            i+=1

        rab_arr.append(b)


print(rab_arr[-1],"last b value")





total = str(b)
# print(b)
# print(mode)
# print(mode.split()[0])


f = open("D:/Documents/python_projects/Rosalind/rosalind_fib_ans.txt", "w+")
for x in total:
    f.write(x)
f.close()