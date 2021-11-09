
import os

myFile = ['account.txt', 'details.csv', 'invite.docx']

for fileName in myFile:
    print(os.path.join('D:\Python\AutomateTheBoringStuffWithPython', fileName))