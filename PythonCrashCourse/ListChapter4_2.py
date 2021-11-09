for valu in range(1, 5):
    print(valu)


for valu2 in range(1, 25, 2):
    print(valu2)


number = list(range(1, 7))
print(number)


even_number = list(range(2, 27, 2))
print(even_number)


suqres = []
for valu in range(1, 11):
    squ = valu ** 2
    suqres.append(squ)
print(suqres)


suqres2 = [valu ** 2 for valu in range(11, 15)]
print(suqres2)
