import re

def make_ngram(sequence, mode):
    """
    sequence : sequece (i.e. string, list...) \n
    mode     : word (w) or letter (l)
    """
    if mode == 'w':
        splited = re.split('[\s,.]', sequence) 
        return [splited[i]+splited[i+1] for i in range(len(splited)-1)]
    elif mode == 'l':
        return [sequence[i]+sequence[i+1] for i in range(len(sequence)-1)]
    else:
        return "plese specify a mode \'w\' or \'l\'"

s1 = "paraparaparadise"
s2 = "paragraph"
X = set(make_ngram(s1, 'l'))
Y = set(make_ngram(s2, 'l'))
sum_union = X | Y
prod_union = X & Y
diff_union = X - Y
print(X)
print(Y)
print(sum_union)
print(prod_union)
print(diff_union)

if "se" in X:
    print('Yes')
else:
    print('No')
    
if "se" in Y:
    print('Yes')
else:
    print('No')
