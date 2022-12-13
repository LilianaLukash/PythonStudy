while True:
    in1 = input("Введіть текст ")
    for sm in in1:
        if sm.isdigit():
            a = int(sm)%2
            match a:
                case 0:
                    print(f"парне число {sm}")
                case _:
                    print(f'непарне число {sm}')
        elif sm.isalnum():
            if sm.isupper():
                print(f"велика літера {sm}")
            if sm.islower():
                print(f"мала літера {sm}")
        else:
            print(f"це символ {sm}")
    ex = input("якщо хочеш вийти нажми Y ")
    if ex =="Y":
        break