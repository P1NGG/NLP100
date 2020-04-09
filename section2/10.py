filename = "popular-names.txt"

line_num = 0
with open(filename) as f:
    for line in f:
        line_num += 1
print(line_num)

# cat popular-names.txt | wc -l