# Repeat program 4 for a list of such words to be censored.
words = ['donkey','are','hello']

with open("donkey.txt", 'r') as f:
    data = f.read()

for word in words:
    data = data.replace(word, "#####")

with open("donkey.txt", 'w') as f:
    f.write(data)