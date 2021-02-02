f=open("D:/Documents/python_projects/Rosalind/rosalind_fib.txt", "r")
if f.mode == 'r':
    mode = f.read()
f.close()

r=1
F=int(mode.split()[1])
n=int(mode.split()[0])

total = 0
a=1
b=1
c=0
for x in range(n):
    if x < 2:
        b=1
        print(x,b)
    else:
        c = b
        b = b + a*F
        a = c
        print(x,b)


total = str(b)
# print(b)
# print(mode)
# print(mode.split()[0])


f = open("D:/Documents/python_projects/Rosalind/rosalind_fib_ans.txt", "w+")
for x in total:
    f.write(x)
f.close()