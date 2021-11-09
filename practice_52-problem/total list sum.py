def add_number(numbers):
    result = 0
    for number in numbers:
        result += number
    return result

x = add_number([1,2,30,4,5,9])
print(x)