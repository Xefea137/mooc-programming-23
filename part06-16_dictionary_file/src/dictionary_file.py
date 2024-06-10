# Write your solution here
def main():
    while True:
        print("1 - Add word, 2 - Search, 3 - Quit")
        function = int(input("Function: "))
        if function == 1:
            fin_w = input("The word in Finnish: ")
            eng_w = input("The word in English: ")
            with open("dictionary.txt", "a") as a_file:
                a_file.write(f"{fin_w};{eng_w}\n")
                print("Dictionary entry added")

        if function == 2:
            search = input("Search term: ")
            with open("dictionary.txt") as file:
                for row in file:
                    part = row.split(";")
                    for item in part:
                        if search in item:
                            print(f"{part[0]} - {part[1]}")

        if function == 3:
            print("Bye!")
            break
main()