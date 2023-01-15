import time

def mydecor(function):
    def wrapper(*args, **kwargs):

        with open("function_calls.txt", "a") as f:
            print(f"{function.__name__} called at {time.time()}\n", file=f)
        return function(*args, **kwargs)
    return wrapper

@mydecor
def my_function(a):
    print(f'Yo hooo {a}')

my_function(5)
