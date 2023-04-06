"""what is the probability that a randomly constructed string will match the given string exactly"""
import math

dna = "AAGAAGATCGTCATCTCCCGATCTTTCCCTCATACAGCCCAATTACGCCTGAGGCTGTCTTAAGGTCTAGCACGTCCTCGACGTGAACCAAGTGCTC"
num_lst = "0.078 0.143 0.220 0.273 0.365 0.437 0.495 0.523 0.607 0.663 0.695 0.758 0.822 0.919"
gc_content = [float(i) for i in num_lst.split()]


outputs = []
prob = 0
for gc in gc_content:
    prob = 0
    chances = {"A": (1 - gc) / 2, "C": gc / 2, "G": gc / 2, "T": (1 - gc) / 2}
    for char in dna:
        prob = prob + math.log10(chances.get(char))
    outputs.append(prob)

print(" ".join([str(i) for i in outputs]))
# ->-86.25282615536167 -74.58300907576282 -67.15032921184341 -63.89965991699372 -60.354901267859596 -58.90194317287187 -58.41495486115068
#    -58.384461321157055 -59.10402515799823 -60.32562781821462 -61.3385769006015 -64.17712709672315 -68.68657859388563 -82.33533812280399
