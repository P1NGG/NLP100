import re

origin = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
string = [s for s in re.split('[\s,.]', string=origin) if not s == '']
extract_one = [0, 4, 5, 6, 7, 8, 14, 15, 18]
elems = {}
for i in range(len(string)):
    if i in extract_one:
        elems[string[i][0]] = i+1
    else:
        elems[string[i][:2]] = i+1
print(elems)