# 1
expense_list = [2340, 2500, 2100, 3100, 2980]

total = 0
for items in expense_list:
    total += items
print(total)


#2
for i in range(1, 11):
    print(i)


#3
for i in range(1, 11):
    print(i * i)


# 4
expense_list = [2340, 2500, 2100, 3100, 2980]

total = 0
for i in range(len(expense_list)):
    print(f"Month {i} Expense {expense_list[i]}")

    total += expense_list[i]
print(f"Total Expense {total}$ USD")


# 5
key_loc = "d"
loc = ['a', 'b', 'c', 'd', 'e']

for i in loc:
    if i == key_loc:
        print(f"Your key loc = {i} found.")
        break

    else:
        print("No found Our Database")

6
for i in range(1, 9):
    if i % 2 == 0:
        continue
    print(i * i)