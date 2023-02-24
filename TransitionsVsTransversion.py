"""Transition is Purine to Purine or pyrimidine to pyrimidine, Transversion is purine to pyrimidine or vise versa.
this code base is finding the  transition/transversion ratio between two strings that have mutated"""

dnastrands = []
sequence = ''
path = r"C:\Users\jelvig\Downloads\rosalind_tran.txt"
with open(path, 'r') as f:
    for line in f:
        if line[0] == '>':
            if sequence:
                dnastrands.append(sequence)
            sequence=''
        else:
            sequence+=line.replace('\n', '')
    dnastrands.append(sequence)

#dnastrands = ['GCAACGCACAACGAAAACCCTTAGGGACTGGATTATTTCGTGATCGTTGTAGTTATTGGAAGTACGGGCATCAACCCAGTT', 'TTATCTGACAAAGAAAGCCGTCAACGGCTGGATAATTTCGCGATCGTGCTGGTTACTGGCGGTACGAGTGTTCCTTTGGGT']

Transitions = ['AG', 'GA', 'CT','TC']
S1 = 0
S2 = 0

for x,y in zip(dnastrands[0], dnastrands[1]):
    if x != y:
        if f'{x}{y}' in Transitions:
            S1 += 1
        else:    
            S2 += 1

print(S1/S2)    # -> 1.21428571429
