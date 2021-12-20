# Exceptions are errors detected at the time of program execution

def bacis_calculator(n1, n2):
    try:
        result = int(n1) / int(n2)

    except ZeroDivisionError as e:
        print("Division by zero exception")
        result = None
    
    except Exception as e:
        print(f"exception occured: {type(e).__name__}")
        result = None

a = input("Enter the first number: ")
b = input("Enter the second number: ")

z = bacis_calculator(a, b)
print(z)
