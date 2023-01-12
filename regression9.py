# create Fibonacci Recursion
list=[]
def FibRecursion(rnumb):
    if rnumb == 1:
        return 0
    elif rnumb ==2:
        return 1
    else:
        nfib = FibRecursion(rnumb-1)+FibRecursion(rnumb-2)
        return nfib
inpR = int(input("Enter integer for Fibonacci Recursion "))
print(FibRecursion(inpR))

#for i in range(inpR):
#   next= FibRecursion(i+1)
#   list.append(next)



