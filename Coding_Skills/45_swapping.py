# Normal Swapping
a = 111
b = 222

print(f"Befor swapping.\nA: {a} \nB: {b}\n")

temp = a    # temp = 111
a = b   # a = 222
b = temp    # b = 111

print(f"After swapping.\nA: {a} \nB: {b}\n")

# Python Swapping
a, b = b, a
print(f"After swapping using python.\nA: {a} \nB: {b}")