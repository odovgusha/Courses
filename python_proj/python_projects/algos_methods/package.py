import sys
import os
import operator

# name = input("Enter your name: ")
# os.system("start cmd")
setup = list()
for line in sys.stdin:
    setup.append(tuple(map(int,(line.split()))))
    # print (tuple(map(int,(line.split()))))
# print(setup)
# print(name)
# reader = ((map(int, line.split(())) for line in sys.stdin.decode()))
# print(list(setup))
# stdin = "3 50 60 20 100 50 120 30"
# stdin = stdin.split()
# setup = list(map(int, stdin))


# print(setup)


# n_thgs,vol = next(reader)

sumitems = 0
n_thgs = setup[0][0]
vol = setup[0][1]
# print(n_thgs,vol)
l_thgs = setup[1:]

if n_thgs == 0 or vol == 0:
    ans = 0
else:
    sorted_dict = sorted(l_thgs, key=lambda i: i[0]/float(i[1]), reverse=True)
    backpack = list()
    # print(sorted_dict)
    i = 0

    while vol > 0 and i < n_thgs:
        if vol >= sorted_dict[i][1]:
            # print(vol, "vol1")
            vol = vol - sorted_dict[i][1]
            backpack.append(sorted_dict[i])
            sumitems += sorted_dict[i][0]
            # print(sumitems)
        else:
            # print(vol, "vol")
            # print(sorted_dict[i][1])
            # print("gep",i)
            ratio = vol/sorted_dict[i][1]

            chunkprice = sorted_dict[i][0]*ratio
            # print(chunkprice,vol)
            sumitems += chunkprice
            backpack.append((chunkprice, vol))
            vol = 0
            # print(sumitems)
        i += 1

# print(backpack)
# print(sumitems)
# print(vol)
# print(round(float(sumitems), 5))
# float(sumitems)
# print("{:.3f}".format(sumitems))
# print(type(format(sumitems, '.6f')))
ans = '{:.3f}'.format(sumitems)
print(ans)
# print(sorted_dict)
