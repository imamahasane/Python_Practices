import re
import sqlite3
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
try:
    def main():
        while True:
            user_input = int(input('\t Please Choice Any Option : '))

            if user_input == 1:
                add_contact()

            elif user_input == 2:
                delete_contact()

            elif user_input == 3:
                display_contact()

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
except:
    print("Please Try Again.")
# ---------------Function---------------
# my_list = []
try:
    def record_data():
        con = sqlite3.connect('database.db')
        cur = con.cursor()
        cur.execute("CREATE TABLE my_contact(first_name text, last_name text, number text primary key, email text, address text)")

        con.commit()
        con.close()
except:
    print("Please Try Again.")

try:
    def add_contact():
        print('Add a new Contact')
        first_name = input('First Name: ')
        last_name = input('Last Name: ')
        number = input('Phone Number: ')
        flag = True
        while flag:
            email = input('E-mail: ')
            m = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$',email)  #Copy to google.com

            if m:
                flag = False

            else:
                print("Invalid Email")

        address = input('Address: ')
        def add_contact(FirstName, LastName, MobileNumber, Email, Address):
            con = sqlite3.connect('database.db')
            cur = con.cursor()
            cur.execute("INSERT INTO my_contact VALUES(?,?,?,?,?)", (FirstName, LastName, MobileNumber, Email, Address))

            con.commit()
            con.close()
except:
    print("Please Try Again.")
