f=open("D:/Documents/python_projects/Rosalind/rosalind_prtm.txt", "r")
if f.mode == 'r':
    prot_seq = f.read().rstrip("\n")
f.close()


amin_mass = {}

with open('prot_mass.txt') as f:
   for l in f:
       amin_mass[l.strip().split("   ")[0]] = float(l.strip().split("   ")[1])
       print(l.strip().split("   ")) # three spaces

print(amin_mass)
print(prot_seq)


prot_mass = 0
for i in prot_seq:
    prot_mass += amin_mass[i]

print(prot_mass)

f = open("D:/Documents/python_projects/Rosalind/rosalind_prtm_ans.txt", "w+")
f.write(str(prot_mass))
f.close()