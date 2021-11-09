
while True:
#    print("Who are you?")
    name = input("Who are you? ")
    
    if name != "Joe":
        continue
    
#    print("Hello, Joy. What is the password? (It is a fish.)")
    password = input("Hello, Joy. What is the password? (It is a fish.) :")
    
    if password == "swordfish":
        break
    
print("Access granted.")