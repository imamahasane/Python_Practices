
def calculat_items(valu):
    total = 0
    for i in valu:
        total += i
    return total

a = [111, 222, 333, 444]
b = [999, 888, 777, 666]

bang = calculat_items(a)
print(bang)

bang2 = calculat_items(b)
print(bang2)
