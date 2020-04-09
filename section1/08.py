import re

def cipher(sequence, mode):
    """
    sequence : sequece (i.e. string, list...) \n
    mode     : encryption (e) or decryption (d)
    """
    result = "" 
    if mode == 'e':
        for i in range(len(sequence)):
            if ord(sequence[i]) >= 97 and ord(sequence[i]) <= 122:
                result += chr(219 - ord(sequence[i]))
            else:
                result += sequence[i]
        return result
    elif mode == 'd':
        for i in range(len(sequence)):
            if ord(sequence[i]) >= 97 and ord(sequence[i]) <= 122:
                result += chr(219 - ord(sequence[i]))
            else:
                result += sequence[i]
        return result
    else:
        return "plese specify a mode \'e\' or \'d\'"

s = "I am an NLPer"
print("s = " + s)
encrypted = cipher(s, mode='e')
print("encrypted = " + encrypted)
decrypted = cipher(encrypted, mode='d')
print("decrypted = " + decrypted)