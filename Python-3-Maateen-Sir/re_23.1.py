
import re

my_string = "purle alice@google.com, blah monkey bob@abc.com blah dishwasher"

temp = my_string.split(",")

for phrase in temp:
    result = re.search("([\w\.-])@([\w\.-]+)", phrase)
    print(result.group())