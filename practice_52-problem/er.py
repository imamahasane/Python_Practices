from itertools import product

a = input().split()

aa = list(map(int, a)) 

b = input().split()

bb = list(map(int, b)) 

print(*product(aa, bb))
