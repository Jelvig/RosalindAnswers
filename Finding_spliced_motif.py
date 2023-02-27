"""This was a combination of premade answers, 'finding a motif in dna' and 'RNA splicing',
 difference being combining them to print the index of where they are."""
def preprocess(s, t):
    s_new = ""
    for c in s:
        if c in t:
            s_new += c
    t_new = ""
    for c in t:
        if c in s:
            t_new += c
    return s_new, t_new

def longest_common_subsequence(s, t):
    n = len(s)
    m = len(t)
    L = [[0] * (m+1) for i in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if s[i-1] == t[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
    return L

def backtrack(L, s, t):
    i = len(s)
    j = len(t)
    indices = []
    while i > 0 and j > 0:
        if s[i-1] == t[j-1]:
            indices.append(i)
            i -= 1
            j -= 1
        elif L[i-1][j] >= L[i][j-1]:
            i -= 1
        else:
            j -= 1
    indices.reverse()
    return indices

def spliced_motif(s, t):
    s_new, t_new = preprocess(s, t)
    L = longest_common_subsequence(s_new, t_new)
    indices = backtrack(L, s_new, t_new)
    return indices


s = """TCCTGTATTCGCTTTTGGTCGCATGATACCGTCTGAGACCACACAATGTAATGAGGCGGT
ACTCGCTTGGACTATATAATTACATTTCATGGTTGATGGGAGCGTTGCGGAGTTGACCCC
TGTTGTAATACGGGCTTTGGCAGGCATTTAACAGAACAATACGTTCTAAGCGGCTGCACA
ACGTTATCCCTGGATGATGTCCCATGCGAAACTTGAGGTGACATCCCAGAGGTTGATAAA
GAATGAAAATACAACCCGGAGCACTGTACGGGTTGCCGCCCAGACTGGGCGGTCTATTTG
AAGGCGACATCTTACTTGTCGCGTATTCGCACAAGAAATCAGCGCGCCGTCCCCTATGGG
ACCATATTAAGGATCGATGGGGGGTTTATACCTAAGTAACTCTTGACCCACACAACTTCT
GTGCGGTAATCGCCTCATTAACCCCAACTTATGATGCGCCTAGCCACTCTTTTAAGGCGA
AACCTTAGGGAGGAAGGATTTTCCGATTCTGTGGTGTCGGGAACCGAGTTAGTATTGCTG
AAATCAGCCTTCTCCCATGGGCTAAATTGTCTAAGCCTATAGGCATATCGACTCCAGGCC
AAAGGTCCTGAGCAGCTGGGCCCCCCCGCCCCCAGAGCATGAATTATATTCCTCCCTTCC
CCTAACCCCTCCACCAAATGACTGCTATGCCTCCCCTGAACATCCGTCTTCAGCGCTGGG
GTAACGATAAGCATTTCACTGTTAGGTAATGCGCTCTCGAAATGGACATCTCCATCGCAA
GTAATTGGCACCACTTCGGGAGTGCCCGCAACAGCCAAGTTAAGCCTTACTTTTTACCCC
GGATGTCCCAAACTCGTGCGCTTCACCTCGCCGTGGTGGCTGCTTGGGCATCGTGCCCTT
TACCGGAGTCAGTTTCTGTGGACCGCAGACTTAATTCAGGTAGGCTTTAAGAGCTCTCGG
CAAATGTCTCTCGGGTTCGAGCCTGTAA"""
t = "GCACTTCGAGTGTATTGACTACAACTTCC"
indices = spliced_motif(s, t)
print(" ".join(str(i) for i in indices))      
# answer -> 888 889 890 898 900 901 904 908 911 918 919 928 932 934 935 936 940 942 945 948 952 961 963 964 972 976 977 982 983



