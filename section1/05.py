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

s = "I am an NLPer"
print(make_ngram(s, 'w'))
print(make_ngram(s, 'l'))
print(make_ngram(s, 'a'))