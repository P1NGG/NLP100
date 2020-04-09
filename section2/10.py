line_num = 0
filename = "popular-names.txt"
with open(filename) as f:
    for line in f:
        line_num += 1
print(line_num)

# cat popular-names.txt | wc -l