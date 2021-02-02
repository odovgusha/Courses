import re
import numpy as np


f=open("D:/Documents/python_projects/Rosalind/rosalind_grph.txt", "r")
# f=open("D:/Documents/python_projects/Rosalind/test.txt", "r")
if f.mode == 'r':
    text = f.read()
f.close()

text = text.replace("\n", "")
print(text)

# crhom_name = re.search(r"Rosalind_\d{4}", text).group()
# print(crhom_name)
t = (re.split(r'(>Rosalind_[0-9]{1,4})', text))[1:]

crhom_names = list()
strings = list()


for i in range(0,len(t),2):
    crhom_names.append(t[i].replace('>', ''))
    strings.append(t[i+1])



print(crhom_names)
print(strings)



# t = (re.split(r'>Rosalind_[0-9]{1,4}', text))
k=3
# print(t)
# print(crhom_names[0])

# with open("D:/Documents/python_projects/Rosalind/rosalind_grph_ans.txt", "w") as f:
#     for i in range(0, len(strings)):
#         for j in range(0, len(strings)):
#         # if t[i][0:3] == t[i][-3:]
#         # print(t[i][0:3])
#         # print(t[i][-3:])
#         #     if strings[i][0:3] == strings[j][-3:]:
#             if strings[i][-3:] == strings[j][0:3]:
#                 # print(crhom_names[i])
#                 # print(crhom_names[i], crhom_names[j])
#                 if crhom_names[i] != crhom_names[j]:
#                     f.write(' '.join([str(crhom_names[i]), str(crhom_names[j]), "\n"]))
#                     # print(crhom_names[i], crhom_names[j], "test")
#                     # print(' '.join([str(crhom_names[i]), str(crhom_names[j])]))
#                      # print(i,j)


# with open("D:/Documents/python_projects/Rosalind/rosalind_grph_str_ans.txt", "w") as f:
#     for i in range(0, len(strings)):
#         for j in range(0, len(strings)):
#         # if t[i][0:3] == t[i][-3:]
#         # print(t[i][0:3])
#         # print(t[i][-3:])
#         #     if strings[i][0:3] == strings[j][-3:]:
#             if strings[i][-3:] == strings[j][0:3]:
#                 # print(crhom_names[i])
#                 # print(crhom_names[i], crhom_names[j])
#                 if strings[i] != strings[j]:
#                     f.write(' '.join([str(strings[i][]), str(strings[j]), "\n"]))
#                     # print(crhom_names[i], crhom_names[j], "test")
#                     # print(' '.join([str(crhom_names[i]), str(crhom_names[j])]))
#                      # print(i,j)
