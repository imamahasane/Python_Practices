def print_int(my_function):
    def any_function():
        return my_function
    
    return any_function()

@print_int
def get_int_as_str(number):
    print(str(number))
    return

get_int_as_str(130)