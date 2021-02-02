import re
import numpy as np

# f=open("D:/Documents/python_projects/Rosalind/rosalind_test.txt", "r")
f=open("D:/Documents/python_projects/Rosalind/rosalind_cons.txt", "r")
if f.mode == 'r':
    text = f.read()
f.close()

text = text.replace("\n", "")
print(text)

t = (re.split(r'>Rosalind_[0-9]{1,4}', text))[1:]
print(t)

larr = len(t[0])
A_arr = [0] * larr
T_arr = [0] * larr
G_arr = [0] * larr
C_arr = [0] * larr
print(larr)

for l in t:
    print(l)
    for i in range(0, larr):
        if l[i] == "A":
            A_arr[i] += 1
        elif l[i] == "T":
            T_arr[i] += 1
        elif l[i] == "G":
            G_arr[i] += 1
        elif l[i] == "C":
            C_arr[i] += 1
# print(A_arr,"test")

m_arr = []
for i in range(0, larr):
    m_c = np.argmax([A_arr[i], T_arr[i], G_arr[i], C_arr[i]])
    # print(m_c)
    if m_c == 0:
        m_arr.append("A")
    elif m_c == 1:
        m_arr.append("T")
    elif m_c == 2:
        m_arr.append("G")
    elif m_c == 3:
        m_arr.append("C")

#
print("A: " + " ".join(map(str,A_arr)).replace(",", ""))
print("T: " + " ".join(map(str,T_arr)).replace(",", ""))
print("G: " + " ".join(map(str,G_arr)).replace(",", ""))
print("C: " + " ".join(map(str,C_arr)).replace(",", ""))

A_sarr = ("A: " + " ".join(map(str,A_arr)).replace(",", "") + "\n")
T_sarr = ("T: " + " ".join(map(str,T_arr)).replace(",", "") + "\n")
G_sarr = ("G: " + " ".join(map(str,G_arr)).replace(",", "") + "\n")
C_sarr = ("C: " + " ".join(map(str,C_arr)).replace(",", "") + "\n")


print("".join(m_arr))
print(len(m_arr))
f = open("D:/Documents/python_projects/Rosalind/rosalind_cons_ans.txt", "w+")
f.write("".join(m_arr) + "\n")
f.write(A_sarr)
f.write(T_sarr)
f.write(G_sarr)
f.write(C_sarr)
f.close()






