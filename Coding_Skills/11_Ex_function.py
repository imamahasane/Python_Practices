def calculate_area(base, height, shape = 'triangle'):

    if shape == 'triangle':
        area = 1 / 2 * (base * height)

    elif shape == 'rectangle':
        area = base * height
    
    else:
        print("sorry!")
        area = None
    
    return area

# Triangle
a = 21
b = 32
reg = calculate_area(a, b, 'triangle')
print(f'Calculate of area is Triangle: {reg}')


# Rectangle
a = 21
b = 32
reg = calculate_area(a, b, 'rectangle')
print(f'Calculate of area is Rectangle: {reg}')

