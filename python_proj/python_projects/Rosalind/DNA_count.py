#seq_samp = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"


f=open("D:/Documents/python_projects/Rosalind/rosalind_dna.txt", "r")
if f.mode == 'r':
    contents = f.read()
f.close()


letters =	{
  "A": 0,
  "C": 0,
  "G": 0,
  "T": 0
}


for x in contents:
    if x == "A":
        letters["A"] += 1
    elif x == "T":
        letters["T"] += 1
    elif x == "G":
        letters["G"] += 1
    elif x == "C":
        letters["C"] += 1

print(letters)

for x in letters:
  print(letters[x], end =" ")

f=open("D:/Documents/python_projects/Rosalind/rosalind_dna_ans.txt", "w+")
for x in letters:
     f.write(str(letters[x]))
     f.write(' ')
f.close()



