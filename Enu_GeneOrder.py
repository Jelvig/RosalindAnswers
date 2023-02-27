from itertools import permutations
per = permutations(range(1,7))
per = list(per)
print(len(per))
for i in per:
    print(*i)  
