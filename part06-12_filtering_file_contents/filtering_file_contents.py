def filter_solutions():
    with open("solutions.csv") as file, open("correct.csv", "w") as c_file, open("incorrect.csv", "w") as ic_file:
        for line in file:
            part = line.split(";")
            if "-" in part[1]:
                y = part[1].split('-')
                result = int(y[0]) - int(y[1])
                if result == int(part[2]):
                    c_file.write(line)
                else:
                    ic_file.write(line)
            elif "+" in part[1]:
                y = part[1].split('+')
                result = int(y[0]) + int(y[1])
                if result == int(part[2]):
                    c_file.write(line)
                else:
                    ic_file.write(line)

if __name__ == "__main__":
    filter_solutions()