file = "rosalind_splc_4.txt"
dna_seq = []
a = 0
parsing = False
with open(file, 'r') as f:
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
            print(new_line)
            new_line = ""
            inRecodingMode = False
        else:
            new_line+=(line.strip())
    else:
        dna_seq.append(new_line)
        

def splicer(dna_seq,introns):
    spliced_dna = ""
    splice_sites = []
    for intr in introns:
        #print(intr)
        for i in range(0,len(dna_seq)):
            if intr == dna_seq[i:i+len(intr)]:
                splice_sites.extend((i,i+len(intr)))
                
    splice_sites.sort()
    include = splice_sites[1:-1]
    spliced_dna += dna_seq[:splice_sites[0]]
    
    include_pairs = list(zip(*[iter(include)]*2))
    #print(include_pairs[0])
    for in_p in include_pairs:
        #print(in_p[0],in_p[1])
        spliced_dna += dna_seq[in_p[0]:in_p[1]]
    #splice_sites[1:-1]
    spliced_dna += dna_seq[splice_sites[-1]:]
    #print(spliced_dna)
    prot = translate(spliced_dna)
    
    return(prot)
        
        
    
    
splicer(dna_seq[0],dna_seq[1:])