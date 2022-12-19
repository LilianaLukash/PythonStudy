phonebook = dict()
commands = ["stats", "add", "delete", "list", "show"]
while True:
    com = (input("Please choose your command: stats, add, delete <name>, list, show <name>")).split()
    print(com)
    if com[0] not in commands:
        print("wrong command")
    else:
        match com[0]:
            case "stats":
                print(f"There are {len(phonebook)} numbers in your phone book ")

            case "add":
                name = input("Please enter new name")
                number = input("Please enter phone number")
                phonebook[name] = number
                print(phonebook)

            case "delete":
                if com[1] in phonebook:
                    phonebook.pop(com[1])
                else:
                    dname = input("Which name you want to delete?")
                    if dname in phonebook:
                        phonebook.pop(dname)
                        print(f"deleted {dname}")
                    else:
                        print("sorry, but no such name")

            case "list":
                for key in phonebook.keys():
                    print(key)

            case "show":
                if com[1] in phonebook:
                    print(phonebook[com[1]])
                else:
                    shname = input("please enter the name ")
                    print(phonebook[shname])

