filename = "popular-names.txt"

line_num = 0
with open(filename) as f:
    for line in f:
        replaced = line.replace('\t', ' ')

# cat popular-names.txt | tr '\t' ' ' 