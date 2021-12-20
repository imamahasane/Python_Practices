a = open("/Users/imamahasan/python/ML_Engineer_Journey/first_read.txt", 'r')
for line in a:
    t = line.split(" ")
    print(str(t))
    
a.close()