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
