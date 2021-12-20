import json

f = open("/Users/imamahasan/python/ML_Engineer_Journey/book.txt", "w+")

phone_book = {}
command = ""

while command != 'exit':
    command = input('Enter a command(new / get / save): ')
    
    if command == "new":
        name = input('Enter name of the person: ')
        phone = input('Phone number: ')
        address = input('Address: ')
        phone_book[name] = {'phone': phone, 'address': address}

    elif command == 'get':
        name = input('Enter name of the person: ')

        if name in phone_book:
            print(phone_book[name])

        else:
            print('Sorry! person not found in address book')

    elif command == 'save':
        f.write(json.dumps(phone_book))
