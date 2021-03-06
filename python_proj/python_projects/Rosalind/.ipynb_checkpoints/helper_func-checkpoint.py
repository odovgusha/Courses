def seq_reader(path):
    file=path
    print("reading ")
    #file = "rosalind_revp.txt"
    dna_seq = []
    a = 0
    parsing = False
    with open(file, 'r') as f:
        print("reading ",file)
        inRecordingMode = False
        new_line = ""
        for line in f:
            if not inRecordingMode:
                if line.startswith('>'):
                    #print(line)
                    inRecordingMode = True
            elif line.startswith('>'):
                #print(line)
                dna_seq.append(new_line)
                #print(new_line)
                new_line = ""
                inRecodingMode = False
            else:
                new_line+=(line.strip())
        else:
            dna_seq.append(new_line)
    return(dna_seq)

def dna2rna(dna_seq):
    rna_seq=""
    for i in range(0,len(dna_seq)):
        if dna_seq[i] == "T":
            rna_seq+="U"
        else:
            rna_seq+=dna_seq[i]
    return(rna_seq)
 
#print(dna2rna("ATGCTTTTGCGCAAA"))

def translate(seq, t_type = 1): 
    table2 = { 
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M', 
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T', 
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K', 
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',                  
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L', 
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P', 
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q', 
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R', 
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V', 
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A', 
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E', 
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G', 
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S', 
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L', 
        'TAC':'Y', 'TAT':'Y', 'TAA':'', 'TAG':'', 
        'TGC':'C', 'TGT':'C', 'TGA':'', 'TGG':'W', 
    }  
    table1 = { 
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M', 
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T', 
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K', 
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',                  
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L', 
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P', 
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q', 
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R', 
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V', 
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A', 
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E', 
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G', 
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S', 
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L', 
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_', 
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W', 
    } 
    
    if t_type==1:
        table = table2
    else:
        table = table1
    protein ="" 
    if len(seq)%3 == 0: 
        for i in range(0, len(seq), 3): 
            codon = seq[i:i + 3] 
            protein+= table[codon] 
    return protein

def rev_c(rev):
    rev_comp=""
    for x in rev:
        if x == "A":
            rev_comp+="T"
        elif x == "T":
            rev_comp+="A"
        elif x == "G":
            rev_comp+="C"
        elif x == "C":
            rev_comp+="G"
    return(rev_comp)

