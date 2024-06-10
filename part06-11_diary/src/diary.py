# Write your solution here
def main():
    while True:
        print("1 - add an entry, 2 - read entries, 0 - quit")
        function = int(input("Function: "))
        if function == 1:
            with open("diary.txt", "a") as file:
                add = input("Diary entry: ")
                file.write(f"{add}\n")
                print("Diary saved")
        if function == 2:
            print("Entries:")
            with open("diary.txt") as file:
                print(file.read())
        if function == 0:
            print("Bye now!")
            break

main()