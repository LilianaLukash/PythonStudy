#factorial recursion
def fact(n):
    if n==1:
        return 1
    else:
        return fact(n-1)*n

numb = int(input("Enter N (int) "))
print(fact(numb))