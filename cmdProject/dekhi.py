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

        elif user_input == 0:
            break

        else:
            print("Your input is wrong. Please try again.\n Thank you so much.")

# ---------------Function---------------
def add_contact():
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

def delete_contact(number):
    try:
        sqliteConnection = sqlite3.connect('SQLite_Python.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sql_update_query = """DELETE from SqliteDb_developers where number = ?"""
        cursor.execute(sql_update_query, (number, ))
        sqliteConnection.commit()

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to delete reocord from a sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()

# deleteSqliteRecord(---)

def show_display_contact():
    try:
        sqliteConnection = sqlite3.connect('SQLite_Python.db')
        cursor = sqliteConnection.cursor()

        sqlite_select_query = """SELECT * from SqliteDb_developers"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        m = len(records))
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
#    if flag is not None
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

# main()

# ---------------Finishing Part---------------
print("\n\n\t\t\t© Copyright 2019, \'Ahasan Software Limited.\' ")
