
s = 'azcbobobegghakl'
c = 0

for value in s:
    if value == 'a' or value == 'e' or value == 'i' or value == 'o' or value == 'u':
        c += 1
print(f"Number of vowels: {c}")