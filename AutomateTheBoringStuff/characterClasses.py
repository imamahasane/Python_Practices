
import re

vowel = re.compile(r'[aeiouAEIOU]')
res = vowel.findall('Robocop eats baby food. BABY FOOD')
print(res)

print('\n============\n')

vowel = re.compile(r'[^aeiouAEIOU]')
res = vowel.findall('Robocop eats baby food. BABY FOOD')
print(res)