a = {'imam': 9123, 'naima': 63719, 'samiul': 93802}
print(a)

a['narail'] = 84021
print(a)

for key in a:
    print(key)

for key in a:
    print(a[key])


for key in a:
    print(f"Key is: {key} and Value is: {a[key]}")


for i, j in a.items():
    print(f"Key is: {i} and Value is: {j}")