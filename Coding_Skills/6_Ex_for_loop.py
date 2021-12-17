
"""
Write a program that asks you to enter an expense amount and program 
should tell you in which month that expense occurred. 
If expense is not found then it should print that as well.
"""

month_list = ["January", "February", "March", "April", "May"]
expense_list = [2340, 2500, 2100, 3100, 2980]
user_expens = int(input("Enter expense amount: "))

month = -1
for i in range(len(expense_list)):
    if user_expens == expense_list[i]:
        month = i
        break

if month != -1:
    print(f"Sir your {user_expens} amount expense is {month_list[month]}")

else:
    print(f"Sorry Sir! your {user_expens} amount not exis our databas")
