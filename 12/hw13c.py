import time
class MyCustomException(Exception):
    def __init__(self):
        self.message = "Custom exception is occured"
        with open("myexeption.txt", "a") as f:
            print(f"{self.__class__.__name__} at {time.time()}", file=f)
        super().__init__(self.message)

raise MyCustomException()