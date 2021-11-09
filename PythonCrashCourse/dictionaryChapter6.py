alien = {'color': 'green', 'points': 5}
print(alien["color"])
print(alien["points"])


alien2 = {'color': 'green', 'points': 5}
print(alien2)
alien2['xp'] = 3
alien2['yp'] = 9
print(alien2)
print(alien2['xp'])


alien3 = {'color': 'green', 'points': 5, 'email': 'mail@gmail.com', 'age': 98}
for key, value in alien3.items():
    print(key)
    print(value)
