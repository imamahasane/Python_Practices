

import pyperclip, re

phoneRegex = re.compile(r'''(
        (\d{3}|\(\d{3}\))    
        (\s|-|\.)?
        (\d{3})
        (\s|-|\.)
        (\d{4})
        (\s*(ext|x|ext.)\s*(\d{2,5}))?
        )''', re.VERBOSE)


emailRegex = re.compile(r'''(
        [a-zA-Z0-9._%+-]+     # username
        @                     # @ symbol
        [a-zA-Z0-9.-]         # domin name
        (\.[a-zA-Z]{2,4})     #dot-something
        )''',re.VERBOSE)


text = str(pyperclip.paste())

matches = []


for group in phoneRegex.findall(text):
    phoneNum = '-'.join([group[1], group[3], group[5]])
    
    if group[8] != '':
        phoneNum += ' x' +group[8]
        
    matches.append(phoneNum)
    
    
for group in emailRegex.findall(text)    :
    matches.append(group[0])
    
    
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard: ')
    print('\n'.join(matches))
    
else:
    print('No phone numbers or email addresses found')
