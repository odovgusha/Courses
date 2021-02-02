f=open("D:/Documents/python_projects/Rosalind/rosalind_hamm.txt", "r")
if f.mode == 'r':
    seq1 = f.readline().rstrip("\n")
    seq2 = f.readline().rstrip("\n")
f.close()


print(seq1[2])
print(seq2[2])

dist = 0

for i in range(1, len(seq1)):
    if seq1[i] != seq2[i]:
        dist += 1


f = open("D:/Documents/python_projects/Rosalind/rosalind_hamm_ans.txt", "w+")
f.write(str(dist))
f.close()