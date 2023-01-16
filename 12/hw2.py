class MyCustomException(Exception):
    def __init__(self):
        self.message = "Custom exception is occured"
        super().__init__(self.message)

raise MyCustomException()
