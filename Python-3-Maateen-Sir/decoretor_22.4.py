
from time import time

def timer(any_function):
    def count_time():
        start = time()
        any_function()
        stop = time()
        print(stop-start, 'seconds')
        return
    return count_time

@timer 
def hello():
    print("hello World!")
    return

@timer 
def another_function():
    for item in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        print(item)
    return

hello()
another_function()
        