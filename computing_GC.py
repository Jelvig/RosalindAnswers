
with open(r"C:\Users\jacob\Downloads\rosalind_gc.txt", "r") as in_file:
    lines = in_file.readlines()
    data = []
    for line in lines:
        data.append(line.splitlines())
    flat_list = [item for i in data for item in i]
    line = ''.join(flat_list)
    in_file.close()

data = line.split(">")
dictionary = {}
data.remove('')
for i in data:
    count = (sum(i.count(x) for x in ("G","C"))/(len([x for x in i]) - 13))*100
    count = "%.6f" % count
    dictionary[i[:13]] = count

print(max(dictionary, key=dictionary.get))
print(max(dictionary.values()))

    
            

