class HighlightBlock:
    def __enter__(self):
        print("==========")
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("==========")
        if exc_val is not None:
            print(f"Error: {exc_val}")
        return True

with HighlightBlock():
    print("This is the block of code being highlighted")
    raise ValueError("An error occurred.")
