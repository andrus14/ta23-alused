text = 'Kuressaare Ametikool'
vowels = 'a, e, i, o, u, õ, ä, ö, ü'.split(', ')
print(vowels)

count = 0

for c in text.lower(): # ametikool
    if c in vowels:
        count += 1 # count = count + 1

print(count)