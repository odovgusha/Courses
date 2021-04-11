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