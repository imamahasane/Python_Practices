
import copy

spam = ['A', 'B', 'C', 'D']
cheese = copy.copy(spam)

cheese[1] = 42
print(spam)
print(cheese)