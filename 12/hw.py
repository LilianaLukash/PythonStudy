def mydecorator(func):
    import time

    def wrapper(*args, **kwargs):
        start = time.time()
        print(start)
        stname = func.__name__
        print(stname)
        return_value = func(*args, **kwargs)
        return return_value
    return wrapper

@mydecorator
def littlefunction():
    print("Ola amigos!")

littlefunction()
