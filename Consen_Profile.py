from collections import Counter
A,G,C,T = [],[],[],[]
def appender(res,A,G,C,T):
    if res.get('A'):
        A.append(res.get('A'))
    else:
        A.append(0)
    if res.get('C'):
        C.append(res.get('C'))
    else:
        C.append(0)
    if res.get('G'):
        G.append(res.get('G'))
    else:
        G.append(0)
    if res.get('T'):
        T.append(res.get('T'))
    else:
        T.append(0)
    return A,C,G,T

dnastrands = []
sequence = ''
path = r"C:\Users\jelvig\Downloads\rosalind_cons.txt"
with open(path, 'r') as f:
    for line in f:
        if line[0] == '>':
            if sequence:
                dnastrands.append(sequence)
            sequence=''
        else:
            sequence+=line.replace('/n', '')
    dnastrands.append(sequence)
    
#print(''.join([Counter(z).most_common(1)[0][0] for z in zip(*dnastrands)]),end='')

cons = [Counter(z).most_common(1)[0][0] for z in zip(*dnastrands)]
cons = filter(lambda x: x != '\n', cons)
print(''.join(cons))

for i in zip(*dnastrands):
    res = Counter(i)
    A,C,G,T = appender(res,A,C,G,T)
print('A: ' + ' '.join(str(x) for x in A))
print('C: ' + ' '.join(str(x) for x in C))
print('G: ' + ' '.join(str(x) for x in G))
print('T: ' + ' '.join(str(x) for x in T))


from collections import Counter

# Define the DNA sequences as a list of strings
dna_strings = []
sequence = ''
path = r"C:\Users\jelvig\Downloads\rosalind_cons.txt"
with open(path, 'r') as f:
    for line in f:
        if line[0] == '>':
            if sequence:
                dna_strings.append(sequence)
            sequence=''
        else:
            sequence+=line.replace('\n', '')
    dna_strings.append(sequence)




"""Best answer to question"""
# # Get the length of the DNA sequences
# n = len(dna_strings[0])

# # Initialize the profile matrix as a dictionary of Counters
# profile_matrix = {
#     'A': Counter(),
#     'C': Counter(),
#     'G': Counter(),
#     'T': Counter()
# }

# # Update the profile matrix with the counts of each nucleotide at each position
# for i in range(n):
#     for dna_string in dna_strings:
#         profile_matrix[dna_string[i]][i] += 1

# # Print the profile matrix
# for nucleotide in ['A', 'C', 'G', 'T']:
#     print(nucleotide + ':', end=' ')
#     for count in profile_matrix[nucleotide].values():
#         print(count, end=' ')
#     print()

# # Compute the consensus sequence by selecting the most common nucleotide at each position
# consensus = ''
# for i in range(n):
#     counts = [profile_matrix[nucleotide][i] for nucleotide in ['A', 'C', 'G', 'T']]
#     consensus += max(zip(counts, ['A', 'C', 'G', 'T']))[1]

# # Print the consensus sequence
# print('Consensus:', consensus)
