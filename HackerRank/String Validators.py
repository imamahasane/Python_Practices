if __name__ == '__main__':
    s = input()

alnum = [ i.isalnum() for i in s]
if True in alnum:
    print("True")
else:
    print("False")

alpha = [ i.isalpha() for i in s]
if True in alpha:
    print("True")
else:
    print("False")

digit = [ i.isdigit() for i in s]
if True in digit:
    print("True")
else:
    print("False")

lower = [ i.islower() for i in s]
if True in lower:
    print("True")
else:
    print("False")

upper = [ i.isupper() for i in s]
if True in upper:
    print("True")
else:
    print("False")