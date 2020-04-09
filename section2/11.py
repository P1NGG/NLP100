filename = "popular-names.txt"
with open(filename) as f:
    for line in f:
        replaced = line.replace('\t', ' ')
        print(replaced, end='')

# cat popular-names.txt | tr '\t' ' '