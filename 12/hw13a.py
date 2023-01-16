import json
phonebook = {"lili":"5555137"}

commands = ["stats", "add", "delete", "list", "show", "exit"]
while True:
    com = (input("Please choose your command: stats, add, delete <name>, list, show <name>, exit ")).split()
    with open("phonebook.json", "r") as book:
        data = book.read()
    phonebook = json.loads(data)

    if com[0] not in commands:
        print("wrong command")
    else:

        match com[0]:
            case "stats":
                print(f"There are {len(phonebook)} numbers in your phone book ")

            case "add":
                name = input("Please enter new name")
                if name not in phonebook:
                    number = input("Please enter phone number")
                    phonebook[name] = number
                    print(phonebook)
                    data = json.dumps(phonebook)
                    print(data)
                    with open("phonebook.json", "w") as book:
                        book.write(data)
                else:
                    print("this name already exist")

            case "delete":
                if com[1] in phonebook:
                    phonebook.pop(com[1])
                    print(f"deleted {com[1]}")
                    data = json.dumps(phonebook)
                    print(data)
                    with open("phonebook.json", "w") as book:
                        book.write(data)
                else:
                    print("sorry, but no such name")

            case "list":
                for key in phonebook.keys():
                    print(key)

            case "show":
                if com[1] in phonebook:
                    print(phonebook[com[1]])
                else:
                    print("sorry, but no such name")

            case "exit":
                break
