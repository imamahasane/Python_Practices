
import re

x = "My number is 415-555-4242."

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
no = phoneNumRegex.search(x)

print('Phone number found: ' + no.group())