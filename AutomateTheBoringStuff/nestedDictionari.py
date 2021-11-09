
allGuests = {'Alice' : {'apple' : 5, 'pretzels' : 12},
             'Bob' : {'ham sandwiches' : 3, 'apples' : 2},
             'Carol' : 3, 'apple pies' : 3}


def totalBrought(guests, item):
    numBrought = 0
    
    for k, v in guests.items():
        numBrought = numBrought + v.get(item, 0)
        
    return numBrought

print('Apples ', str(totalBrought(allGuests, 'apples')))