# dna = "GATGGAACTTGACTACGTAAATT"



f=open("D:/Documents/python_projects/Rosalind/rosalind_rna.txt", "r")
if f.mode == 'r':
    dna = f.read()
f.close()


rna = list()



n=0
for x in dna:
    if x == "A":
        rna.append("A")
    elif x == "T":
        rna.append("U")
    elif x == "G":
        rna.append("G")
    elif x == "C":
        rna.append("C")


print(''.join(rna))
str_rna = ''.join(rna)


f = open("D:/Documents/python_projects/Rosalind/rosalind_rna_ans.txt", "w+")
for x in str_rna:
    f.write(x)
f.close()