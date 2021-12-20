a = open("/Users/imamahasan/python/ML_Engineer_Journey/first_read.txt", 'r')
a_out = open("/Users/imamahasan/python/ML_Engineer_Journey/first_read_wc.txt", 'w')

for line in a:
    t = line.split(" ")
    a_out.write(f"wordcount: {str(len(t))} | {line}")
    
a.close()