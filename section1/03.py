import re

pi = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
words = re.split('[\s,.]', string=pi)
print([len(word) for word in words if not word == ''])