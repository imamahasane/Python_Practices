
import sys, pyperclip

#! python3
#pw.py - A insecure password locker program.

PASSWORDS = {'email' : 'Dgvvwe25r834gvbhsdjkngfjajagvg',
             'blog' : 'kjghbja;jfswsfklj39847t3dgffdh',
             'luggage' : 'sdjkghs873568dfgk34590nbs'}



if len(sys.argv) < 2:
    print('Using: Python pw.py [account] - copy account password')
    sys.exit()
    
account = sys.argv[1]    #First command line arg is the account name


if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')

else:
    print('There is on account named ' + account)