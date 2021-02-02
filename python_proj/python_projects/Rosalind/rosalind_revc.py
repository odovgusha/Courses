# dna = "AAAACCCGGT"


dna = ""
f=open("D:/Documents/python_projects/Rosalind/rosalind_revc.txt", "r")
if f.mode == 'r':
    dna = f.read()
f.close()


rev = list(reversed(dna))
rev_comp = list()

for x in rev:
    if x == "A":
        rev_comp.append("T")
    elif x == "T":
        rev_comp.append("A")
    elif x == "G":
        rev_comp.append("C")
    elif x == "C":
        rev_comp.append("G")


print(''.join(rev_comp))
# str_rna = ''.join(rna)


f = open("D:/Documents/python_projects/Rosalind/rosalind_revc_ans.txt", "w+")
for x in rev_comp:
    f.write(x)
f.close()