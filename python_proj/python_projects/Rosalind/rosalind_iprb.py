f=open("D:/Documents/python_projects/Rosalind/rosalind_iprb.txt", "r")
if f.mode == 'r':
    anim_num = f.readline().split()
f.close()


# anim = list(map(int, anim))
# anim_t = [2,2,2]
# print(anim_t)
# print(anim)
#
#
# prob =  []
# print(range(len(anim_t)))
# for i in range(len(anim_t)):
#     prob.append(anim_t[i]/sum(anim_t))
#
# print(prob)
#
#
# pmate = []
# for i in range(len(prob)):
#     for j in range(len(prob)):
#         pmate.append(prob[i] * prob[j])
#
# print(pmatez)



anim_num = list(map(int, anim_num))
anim_sp = ["11", "10", "00"]
anim = dict(zip(anim_sp, anim_num))
# anim = {"11":2,"10":2,"00":2}



anim_11 = {}
anim_11.update(anim)
anim_11["11"] -= 1

anim_10 = {}
anim_10.update(anim)
anim_10["10"] -= 1

anim_00 = {}
anim_00.update(anim)
anim_00["00"] -= 1


# print(anim_t)
# print(anim)
#
#


prob = {}
for key in anim:
    prob[key] = (anim[key]/sum(anim.values()))
print(prob)

prob11 = {}
for key in anim_11:
    prob11[key] = (anim_11[key]/sum(anim_11.values()))
print(prob11)

prob10 = {}
for key in anim_10:
    prob10[key] = (anim_10[key]/sum(anim_10.values()))
print(prob10)

prob00 = {}
for key in anim_00:
    prob00[key] = (anim_00[key]/sum(anim_00.values()))
print(prob00)


anim_td = anim



pmate = {}
for key1 in anim:
    if key1 == "11":
        prob2 = prob11
    elif key1 == "10":
        prob2 = prob10
    else:
        prob2 = prob00
    for key2 in anim:# Perhaps you should remove on of the elements before!!!
        child = key1+key2
        pmate[child] = (prob[key1] * prob2[key2])
        # print(prob[key1] * prob[key2])

print(pmate)

prob_dom = {}

for key in pmate:
    if key == '1000' or key == '0010':
        prob_dom[key] = pmate[key] * 0.5
    elif key == '1010':
        prob_dom[key] = pmate[key] * 0.75
    elif key == '0000':
        prob_dom[key] = pmate[key] * 0
    else:
        prob_dom[key] = pmate[key]

print(sum(prob_dom.values()))

prob_dom_sum = sum(prob_dom.values())

f = open("D:/Documents/python_projects/Rosalind/rosalind_iprb_ans.txt", "w+")
f.write(str(prob_dom_sum))
f.close()