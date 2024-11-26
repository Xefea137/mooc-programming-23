# Write your solution here
def week_check(w: dict):
    w = w.split(" ")
    try:
        if int(w[1]):
            return True
    except:
        return False

def data_check(d: dict):
    d = d.split(",")
    if len(d) != 7:
        return False

    for item in d:
        try:
            if int(item) and int(item) > 0 and int(item) < 40:
                pass
            else:
                return False
        except:
            return False

    for item in range(7):
        if (d[item]) in d[item+1:7]:
            return False
        
    return True

def filter_incorrect():
    lot = {}
    with open("lottery_numbers.csv") as file, open("correct_numbers.csv", "w") as c_file:
        for row in file:
            row = row.strip()
            data = row.split(";")
            if week_check(data[0]) and data_check(data[1]):
                c_file.write(f"{data[0]};{data[1]}\n")              
                
if __name__ == "__main__":
    filter_incorrect()