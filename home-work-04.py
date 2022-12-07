inp1 = input("введіть ціле число або слово ")
try:
    inp2 = int(inp1)
    print(inp2)
    print("число")
    if inp2 % 2 == 0:
        print("парне")
    else:
        print("непарне")
except:
    print(f"слово довжиною {len(inp1)} знаків")