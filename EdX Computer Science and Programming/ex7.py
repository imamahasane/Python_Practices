
school = 'Massachusetts Institute of Technology'
numVowels = 0
numCons = 0

for i in school:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        numVowels += 1
        
    elif i == 'o' or i == 'M':
        print(i)
        
    else:
        numCons -= 1
        
print('numVowels is: ' + str(numVowels))
print('numCons is: ' + str(numCons))