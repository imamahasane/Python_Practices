import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {str((end-start) * 1000)} mili second.")
        return result
    return wrapper

@time_it
def f_square(number):
    result = []
    for n in number:
        result.append(n * n)
    return result

@time_it
def f_cube(number):
    result = []
    for n in number:
        result.append(n * n * n)
    return result

a = range(1, 100000)

x = f_square(a)
y = f_cube(a) 