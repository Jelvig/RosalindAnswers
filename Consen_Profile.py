"""This question gave several dna strands of equal length and
    I was responsible to find the most common nucleotides in each
    position, and the count of each oligo."""

"different approach correct answer."

def consensus_profile(dna_strings):
    # First, we compute the profile matrix
    profile = [[0] * len(dna_strings[0]) for _ in range(4)]
    for dna in dna_strings:
        for i in range(len(dna)):
            if dna[i] == 'A':
                profile[0][i] += 1
            elif dna[i] == 'C':
                profile[1][i] += 1
            elif dna[i] == 'G':
                profile[2][i] += 1
            elif dna[i] == 'T':
                profile[3][i] += 1
    
    # Next, we compute the consensus sequence
    consensus = []
    for i in range(len(profile[0])):
        max_count = 0
        max_nuc = ''
        for j in range(4):
            if profile[j][i] > max_count:
                max_count = profile[j][i]
                if j == 0:
                    max_nuc = 'A'
                elif j == 1:
                    max_nuc = 'C'
                elif j == 2:
                    max_nuc = 'G'
                elif j == 3:
                    max_nuc = 'T'
        consensus.append(max_nuc)
    
    # Finally, we return the consensus sequence and the profile matrix
    return ''.join(consensus), profile

def fasta_dna():
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
        return dna_strings


dna_strings = fasta_dna()
consensus, profile = consensus_profile(dna_strings)
print(consensus)
nucleo = ['A:','C:','G:','T:']
count = 0
for i in profile:
    print(nucleo[count], end=' ',sep=' ')
    print(*i, sep=' ')
    count+=1



"first approach: gave the same answer but spacing and punctiation is wrong"
# from collections import Counter
# A,G,C,T = [],[],[],[]
# def appender(res,A,G,C,T):
#     if res.get('A'):
#         A.append(res.get('A'))
#     else:
#         A.append(0)
#     if res.get('C'):
#         C.append(res.get('C'))
#     else:
#         C.append(0)
#     if res.get('G'):
#         G.append(res.get('G'))
#     else:
#         G.append(0)
#     if res.get('T'):
#         T.append(res.get('T'))
#     else:
#         T.append(0)
#     return A,C,G,T

# dnastrands = []
# sequence = ''
# path = r"C:\Users\jelvig\Downloads\rosalind_cons.txt"
# with open(path, 'r') as f:
#     for line in f:
#         if line[0] == '>':
#             if sequence:
#                 dnastrands.append(sequence)
#             sequence=''
#         else:
#             sequence+=line.replace('/n', '')
#     dnastrands.append(sequence)
    
# #print(''.join([Counter(z).most_common(1)[0][0] for z in zip(*dnastrands)]),end='')

# cons = [Counter(z).most_common(1)[0][0] for z in zip(*dnastrands)]
# cons = filter(lambda x: x != '\n', cons)
# print(''.join(cons))

# for i in zip(*dnastrands):
#     res = Counter(i)
#     A,C,G,T = appender(res,A,C,G,T)
# print('A: ' + ' '.join(str(x) for x in A))
# print('C: ' + ' '.join(str(x) for x in C))
# print('G: ' + ' '.join(str(x) for x in G))
# print('T: ' + ' '.join(str(x) for x in T))


# from collections import Counter

# # Define the DNA sequences as a list of strings
# dna_strings = []
# sequence = ''
# path = r"C:\Users\jelvig\Downloads\rosalind_cons.txt"
# with open(path, 'r') as f:
#     for line in f:
#         if line[0] == '>':
#             if sequence:
#                 dna_strings.append(sequence)
#             sequence=''
#         else:
#             sequence+=line.replace('\n', '')
#     dna_strings.append(sequence)





