#create Fibonacci Generator
def f_generator(number):
    numb1, numb2 = 0, 1
    for _ in range(number):
        yield numb1
        numb1, numb2 = numb2, numb1+numb2

inp = int(input("Enter integer for Fibonacci Generator "))
gen1 = f_generator(inp)
for _ in range(inp):
    print(next(gen1))



