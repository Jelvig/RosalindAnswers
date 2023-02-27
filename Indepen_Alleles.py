import math

#2**k to get the number of offspring

def prob_dominant(k, n):
    q = 2**k
    prob = 0
    for i in range(n, (q+1)):  # +1 because range starts at 0
        prob += math.comb(q, i) * (0.25**i) * (0.75**(q-i))  # probability of dominant allele given heterozygous parent
                                                             # probability of recessive allele
                                                             # multiplied by the combination of q and i = probablity
    return prob

prob = prob_dominant(6,15)
print("%.3f" % prob)
