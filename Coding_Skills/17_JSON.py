book = {}

book['imam'] = {
    'name': 'Imam',
    'address': 'mirpur-1',
    'phone': 938363
}

book['naima'] = {
    'name': 'naima',
    'address': 'farmgate',
    'phone': 54376
}

book['samiul'] = {
    'name': 'samiul',
    'address': 'narail',
    'phone': 892132
}

import json

a = json.dumps(book)
with open("/Users/imamahasan/python/ML_Engineer_Journey/book.txt", "w") as f:
    f.write(a)


re = open("/Users/imamahasan/python/ML_Engineer_Journey/book.txt", "r")
m = re.read()
print(m)
print(type(m))

import json
book = json.loads(m)
print(book)
print(type(book))

