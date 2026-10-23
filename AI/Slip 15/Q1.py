s = input("Enter string: ")
v = c = d = sp = 0

for ch in s:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            v += 1
        else:
            c += 1
    elif ch.isdigit():
        d += 1
    elif not ch.isspace():
        sp += 1

print("Vowels:", v)
print("Consonants:", c)
print("Digits:", d)
print("Special characters:", sp)