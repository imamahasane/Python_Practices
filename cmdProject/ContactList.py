import re
import sqlite3

try:
    sqliteConnection = sqlite3.connect('SQLite_Python.db')
    cursor = sqliteConnection.cursor()

    sqlite_select_Query = "select sqlite_version();"
    cursor.execute(sqlite_select_Query)
    record = cursor.fetchall()
    cursor.close()

except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)
finally:
    if (sqliteConnection):
        sqliteConnection.close()        
        

try:
    sqliteConnection = sqlite3.connect('SQLite_Python.db')
    sqlite_create_table_query = '''CREATE TABLE SqliteDb_developers (
                                number INTEGER PRIMARY KEY,
                                first_name TEXT NOT NULL,
                                last_name TEXT NOT NULL,
                                email text NOT NULL,
                                address text NOT NULL);'''

    cursor = sqliteConnection.cursor()
    cursor.execute(sqlite_create_table_query)
    sqliteConnection.commit()

    cursor.close()

except sqlite3.Error as error:
    print("Error while creating a sqlite table", error)
finally:
    if (sqliteConnection):
        sqliteConnection.close()
        print("sqlite connection is closed")
        


# ---------------Display---------------
print('\nWelcome To Your Contact List.')
print('----------------------')
print('1. - Add A New Contact.')
print('2. - Delete Any Contact.')
print('3. - Show Display Contacts List.')
print('4. - Search Any Contact.')
#print('5. - Check Version.')
print("5. - Main Manu.")
print('0. - Exit.')
print('----------------------')

# ---------------Main Function---------------
def main():
    while True:
        user_input = int(input('\t Please Choice Any Option : '))

        if user_input == 1:
            add_contact()

        elif user_input == 2:
            delete_contact()

        elif user_input == 3:
            show_display_contact()

        elif user_input == 4:
            search_contact()

        elif user_input == 5:
            user_input
#
#        elif user_input == 5:
#            check_version()

        elif user_input == 0:
            break

        else:
            print("Your input is wrong. Please try again.\n Thank you so much.")

# ---------------Function---------------
my_list = []
def add_contact():
#    print('Add a new Contact')
#    first_name = input('First Name: ')
#    last_name = input('Last Name: ')
#    number = input('Phone Number: ')
#    flag = True
#
#    while flag:
#        email = input('E-mail: ')
#        m = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$',email)  #Copy to google.com
#
#        if m:
#            flag = False
#
#        else:
#            print("Invalid Email")
#
#    address = input('Address: ')
#
#    tmp = []
#    tmp = first_name, last_name, number, email, address
#    my_list.append(list(tmp))
    try:
        sqliteConnection = sqlite3.connect('SQLite_Python.db')
        cursor = sqliteConnection.cursor()
    
        sqlite_insert_query = "INSERT INTO SqliteDb_developers VALUES (?,?,?,?,?)",('first_name', 'last_name', 'number', 'email', 'address') 
    
        count = cursor.execute(sqlite_insert_query)
        sqliteConnection.commit()
        cursor.close()
    
    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")


def delete_contact():
    print('Delete Contact')
    delete_contact_input = input('Enter contact Phone for delete: ')

    flag = None
    for i in my_list:
        for j in i:
            if delete_contact_input == j:
                flag = my_list[my_list.index(i)]
                break

    if flag is not None:
        my_list.remove(flag)

    else:
        print("Not Found")


def show_display_contact():
#    if len(my_list) == 0:
#        print("\n\tYour Contact List Is Empty.\n\tPlease try other options")
#
#    else:
#        print('Show display Contact List')
#        count = 0
#
#        for i in my_list:
#            count += 1
#            print(count)
#            print("first_name: ", i[0])
#            print("last_name: ", i[1])
#            print("number: ", i[2])
#            print("email: ", i[3])
#            print("address: ", i[4])
#            print("----------")
        try:
        sqliteConnection = sqlite3.connect('SQLite_Python.db')
        cursor = sqliteConnection.cursor()

        sqlite_select_query = """SELECT * from SqliteDb_developers"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        print("Total rows are:  ", len(records))
        print("Printing each row")
        for row in records:
            print("first_name: ", row[0])
            print("last_name: ", row[1]) 
            print("number: ", row[2])
            print("email: ", row[3])
            print("address: ", row[4])
            print("\n")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")

show_display_contact()

#def search_contact():
#    print('Search A Contact')
#    search_input = input('Please enter your input: ')
#
#    flag = None
#    for i in my_list:
#        for j in i:
#            if search_input == j:
#                flag = my_list[my_list.index(i)]
#                break
#
#    if flag is not None:
#        #print(flag)
#        print("first_name: ", flag[0])
#        print("last_name: ", flag[1])
#        print("number: ", flag[2])
#        print("email: ", flag[3])
#        print("address: ", flag[4])
#
#    else:
#        print("Not Found")
#

main()

# ---------------Finishing Part---------------
print("\n\n\t\t\t© Copyright 2019, \'Ahasan Software Limited.\' ")
