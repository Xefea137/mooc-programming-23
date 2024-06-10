# Write your solution here
def phone_book_application():
    phonebook = {}
    while True:
        option = int(input("command (1 search, 2 add, 3 quit): "))
        if option == 1:
            search_name = input("name: ")
            if search_name in phonebook:
                print(phonebook[search_name])
            else:
                print("no number")

        elif option == 2:
            add_name = input("name: ")
            number = input("number: ")
            phonebook[add_name] = number
            print("ok!")

        elif option == 3:
            print("quitting...")
            break

phone_book_application()