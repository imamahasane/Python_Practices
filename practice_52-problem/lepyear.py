u_input = int(input("Please enter your input: "))

if u_input % 400 == 0:
    print(u_input, "year is a leapyer.")
    
elif u_input % 100 == 0:
    print(u_input, "year is not a leapyer.")
    
elif u_input % 4 == 0:
    print(u_input, "year is a lepyer.")
    
else:
    print("Sorry! your input is wrong.Please try again.")