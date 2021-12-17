# 1
num = input("Enter a number: ")
num = int(num)

if num % 2 == 0:
    print(num, "number is even")

else:
    print(num, "number is odd")

# 2
india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

dish = input("Please Enter your Dish name: ")

if dish in india:
    print(f"Your Dish {dish} is Indian")

elif dish in pakistan:
    print(f"Your Dish {dish} is Pakistan")

elif dish in bangladesh:
    print(f"Your Dish {dish} is Bangladesh")

else:
    print(f"Your dish '{dish}' cannot be found in our database")