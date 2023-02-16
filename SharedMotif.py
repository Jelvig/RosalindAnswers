dnastrands = []
sequence = ''
path = r"C:\Users\jelvig\Downloads\rosalind_lcsm.txt"
with open(path, 'r') as f:
    for line in f:
        if line[0] == '>':
            if sequence:
                dnastrands.append(sequence)
            sequence=''
        else:
            sequence+=line.replace('/n', '')
    dnastrands.append(sequence)
dnastrands = [x.replace('\n','') for x in dnastrands]

srt_seq = sorted(dnastrands, key=len)     

first_seq = srt_seq[0]     #  comparing only the first strand vs the rest              
compiled_seq = srt_seq[1:]                   
motif = ''                               
for i in range(len(first_seq)):          
    for j in range(i, len(first_seq)):   
        motif_temp = first_seq[i:j + 1]   #  accessing characters        
        found = False                   
        for sequ in compiled_seq:            
            if motif_temp in sequ: # do the characters exist in the other sequences?               
                found = True            
            else:                        
                found = False           
                break                   
        if found and len(motif_temp) > len(motif):   # only keep the longest motif that is found
            motif = motif_temp                    
print(motif)
