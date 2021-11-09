
catName = []
while True:
    print("Enter the name of cat " +str(len(catName) + 1)+ " (Or enter nothing to stop): ")
    name = input()
    
    if name == '':
        break
    
    catName = catName + [name]
    
print("The cat names are: ")

for name in catName:
    print(" " + name)