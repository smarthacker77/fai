s = input("Enter a string: ")
words = s.split()
d = {}

for word in words:
    d[word] = d.get(word, 0) + 1

print(d)