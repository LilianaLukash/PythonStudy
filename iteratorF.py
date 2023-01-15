#fibonacci iterator
count = 0
class MyIterator:
    def __init__(self, numb):

        self.a = 0
        self.b = 1
        self.numb = numb

    def __iter__(self):
        return self

    def __next__(self):
        fib = self.a
        count =+1
        self.a, self.b = self.b, self.a + self.b
        if count >= self.numb:
            raise StopIteration
        return fib

numb = int(input("Enter integer "))
objf= MyIterator(numb)
print(objf)
for x in range(numb):
    if x == numb-1:
        print(next(objf))
    else: next(objf)

