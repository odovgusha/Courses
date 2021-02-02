f=open("D:/Documents/python_projects/Rosalind/rosalind_subs.txt", "r")
if f.mode == 'r':
    seq = f.readline().rstrip("\n")
    sub_seq = f.readline().rstrip("\n")
f.close()

# seq = "GATATATGCATATACTT"
# sub_seq = "ATAT"


lss = len(sub_seq)
match = []
for i in range(0, len(seq)-lss+1):
    if seq[i:(lss+i)] == sub_seq:
        match.append(i+1)



# match_str = ' '.join(map(str, match))
# print(match_str)
# out = match_str

f = open("D:/Documents/python_projects/Rosalind/rosalind_subs_ans.txt", "w+")
f.write(match_str)
f.close()