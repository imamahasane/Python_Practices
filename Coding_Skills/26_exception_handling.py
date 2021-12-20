
# Exceptions are errors detected at the time of program execution
def bacis_calculator(n1, n2):
    try:
        result = n1 / n2
    
    except Exception as e:
        print(f"exception occured: {e}")
        result = None

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

z = bacis_calculator(a, b)
print(z)

