# Write your solution here
def phone_book_application():
    phonebook = {}
    while True:
        option = int(input("command (1 search, 2 add, 3 quit): "))
        if option == 1:
            search(phonebook)
        elif option == 2:
            add(phonebook)
        elif option == 3:
            print("quitting...")
            break

def search(phonebook):
    search_name = input("name: ")
    if search_name in phonebook:
        for key, value in phonebook.items():
            if key == search_name:
                for item in value:
                    print(item)
    else:
        print("no number")
        
def add(phonebook):
    add_name = input("name: ")
    number = input("number: ")
    if add_name not in phonebook:
        phonebook[add_name] = []
    phonebook[add_name].append(number)
    print("ok!")

phone_book_application()