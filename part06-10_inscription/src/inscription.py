# Write your solution here
def main():
    name = input("Whom should I sign this to: ")
    save = input("Where shall I save it: ")
    with open(save, "w") as file:
        file.write(f"Hi {name}, we hope you enjoy learning Python with us! Best, Mooc.fi Team")

    with open(save) as file:
        print(file.read())

main()