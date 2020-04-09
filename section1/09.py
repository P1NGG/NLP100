import random

def typoglycemia(sequence):
    words = sequence.split(' ') 
    for i in range(len(words)):
        if len(words[i]) >= 5:
            shuffled = ''.join(random.sample(words[i][1:-1], len(words[i][1:-1])))
            words[i] = words[i][0] + shuffled + words[i][-1]
    return words

text = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
print(typoglycemia(text))