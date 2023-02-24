codon = {'UUU': 'F', 'CUU': 'L', 'AUU': 'I', 'GUU': 'V',
            'UUC': 'F', 'CUC': 'L', 'AUC': 'I', 'GUC': 'V',
            'UUA': 'L', 'CUA': 'L', 'AUA': 'I', 'GUA': 'V',
            'UUG': 'L', 'CUG': 'L', 'AUG': 'M', 'GUG': 'V',
            'UCU': 'S', 'CCU': 'P', 'ACU': 'T', 'GCU': 'A',
            'UCC': 'S', 'CCC': 'P', 'ACC': 'T', 'GCC': 'A',
            'UCA': 'S', 'CCA': 'P', 'ACA': 'T', 'GCA': 'A',
            'UCG': 'S', 'CCG': 'P', 'ACG': 'T', 'GCG': 'A',
            'UAU': 'Y', 'CAU': 'H', 'AAU': 'N', 'GAU': 'D',
            'UAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D',
            'UAA': 'Stop', 'CAA': 'Q', 'AAA': 'K', 'GAA': 'E',
            'UAG': 'Stop', 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E',
            'UGU': 'C', 'CGU': 'R', 'AGU': 'S', 'GGU': 'G',
            'UGC': 'C', 'CGC': 'R', 'AGC': 'S', 'GGC': 'G',
            'UGA': 'Stop', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G',
            'UGG': 'W', 'CGG': 'R', 'AGG': 'R', 'GGG': 'G' }

dnastrands = []
sequence = ''
path = r"C:\Users\jelvig\Downloads\rosalind_splc.txt"
with open(path, 'r') as f:
    for line in f:
        if line[0] == '>':
            if sequence:
                dnastrands.append(sequence)
            sequence=''
        else:
            sequence+=line.replace('\n', '')
    dnastrands.append(sequence)

#dnastrands = ['ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG', 'ATCGGTCGAA', "ATCGGTCGAGCGTGT"]
exon = dnastrands[0]
introns = dnastrands[1:]
for i in introns:
    exon = exon.replace(i, '')

exon = exon.replace('T','U')
dna_chunks = [exon[i:i+3] for i in range(0, len(exon), 3)]

for i in dna_chunks:
    if i in codon.keys():
        print(codon.get(i), end='')
        if codon.get(i) == 'Stop':  # -> MVYIADKQHVASREAYGHMFKVCAStop
            break
