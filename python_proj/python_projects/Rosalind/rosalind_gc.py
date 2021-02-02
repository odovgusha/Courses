import re


chromGC = {}
numGC = 0
numBP = 0 ## repair it later


f=open("D:/Documents/python_projects/Rosalind/rosalind_gc.txt", "r")
# f=open("D:/Documents/python_projects/Rosalind/test.txt", "r")
while True:
    # read a single line
    line = f.readline()
    print(not line, numBP > 0)
    if not line:
        print("not a line")
        chromGC[crhom_name] = numGC * 100 / numBP
        print(numGC,numBP,chromGC[crhom_name])
        break
    # if line[0:9] == ">Rosalind" and not bool(chromGC):  # avoid processing the first few lines start with @
    if line[0:9] == ">Rosalind" and numBP > 0:

        chromGC[crhom_name] = numGC * 100 / numBP
        print(chromGC[crhom_name])
        crhom_name = re.search(r"Rosalind_\d{4}", line).group()
        chromGC[crhom_name] = 0
        numGC = 0
        numBP = 0
    elif line[0:9] == ">Rosalind" and numBP == 0:

        crhom_name = re.search(r"Rosalind_\d{4}", line).group()
        chromGC[crhom_name] = 0
        numGC = 0
        numBP = 0
    else:
        for c in line:
            if c == "C" or c == "G":
                numGC += 1
                numBP += 1
            if c == "A" or c == "T":
                numBP += 1

f.close()



# print(bool(re.match(r">Rosalind_[0-9]+", '>Rosalind_1')))
# print(bool(re.match(r">Rosalind_\d{4}", '>Rosalind_2234')))



max_chrom_n = max(chromGC, key=chromGC.get)
max_chromGC = str(format(chromGC[max_chrom_n], '.6f'))



f = open("D:/Documents/python_projects/Rosalind/rosalind_gc_ans.txt", "w+")
f.write(max_chrom_n)
f.write("\n")
f.write(max_chromGC)
f.close()



#
#
#
# print((0.6065573770491803 + 0.5925925925925926)/2, "test")
#
# test1 = "CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC"
# test2 = "TGGGAACCTGCGGGCAGTAGGTGGAAT"
# test3 = "CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT"
#
# numGC = 0
# for c in test1:
#     if c == "C" or c == "G":
#         numGC += 1
#
# print(numGC,len(test1),numGC/len(test1))
# numGC = 0
#
# for c in test2:
#     if c == "C" or c == "G":
#         numGC += 1
#
# print(numGC,len(test2),numGC/len(test2))
#
#
# numGC = 0
#
# for c in test3:
#     if c == "C" or c == "G":
#         numGC += 1
#
# print(numGC,len(test3),numGC/len(test3))
#
#
#






#
#
# mode.split(r'>Rosalind_\d{4}$')
#
#
# for item in re.split(r">Rosalind_\d{4}", mode):
#     print(item)
#
#
# print(bool(re.match(r">Rosalind_[0-9]+", '>Rosalind_1')))
# print(bool(re.match(r">Rosalind_\d{4}", '>Rosalind_2234')))
# {1}

#
# chromGC = {}
# # f=open("D:/Documents/python_projects/Rosalind/rosalind_gc.txt", "r")
# f=open("D:/Documents/python_projects/Rosalind/test.txt", "r")
# if f.mode == 'r':
#     for line in f:
#         l_contGC = 0
#         numGC = 0
#         if line[0:9] == ">Rosalind":  # avoid processing the first few lines start with @
#             numGC = 0
#             # print(line)
#             crhom_name = line
#             chromGC[crhom_name] = 0
#             continue
#
#         for c in line:
#             if c == "C" or c == "G":
#                 numGC += 1
#         l_contGC = numGC/len(line)
#         # print(l_contGC)
#         chromGC[crhom_name] = (chromGC[crhom_name] + l_contGC)/2


#
# f=open("D:/Documents/python_projects/Rosalind/test.txt", "r")
# if f.mode == 'r':
#     for line in f:
#
#         if line[0:9] == ">Rosalind":  # avoid processing the first few lines start with @
#             # print(line)
#             if not bool(chromGC):
#                 crhom_name = line
#                 chromGC[crhom_name] = 0
#             else:
#                 chromGC[crhom_name] = numGC/numBP
#                 numBP = 0
#                 numGC = 0
#             crhom_name = line
#             chromGC[crhom_name] = 0
#             continue
#
#         for c in line:
#             if c == "C" or c == "G":
#                 numGC += 1
#
#         print(numGC,len(line))
#         print(line)
#         numBP += len(line)


f.close()