def print_dict(**kwargs):
    print(kwargs)
    for args in kwargs:
        print("{} : {}".format(args, kwargs[args]))
        
print_dict(a = 1, b = 2, c = 3)