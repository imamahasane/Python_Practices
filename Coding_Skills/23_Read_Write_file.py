
with open("/Users/imamahasan/python/ML_Engineer_Journey/first_read.txt", 'r') as f:
    print(f.read())

# You don't need to do "f.close()" if you use "with". Using "with" will automatically close the file .
print(f.closed)