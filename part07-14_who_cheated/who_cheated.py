# Write your solution here
import csv
from datetime import datetime, timedelta
def cheaters():
    cheaters_list = []
    data = {}
    
    with open("start_times.csv") as start, open("submissions.csv") as finish:
        for line in csv.reader(start, delimiter=";"):
            data[line[0]] = {"start" : datetime.strptime(line[1], "%H:%M"), "end" : datetime.strptime(line[1], "%H:%M")}

        for lines in csv.reader(finish, delimiter=";"):
            if lines[0] in data:
                if datetime.strptime(lines[3], "%H:%M") > data[lines[0]]['end']:
                    data[lines[0]]['end'] = datetime.strptime(lines[3], "%H:%M")

        for name, value in data.items():
            if (value['start']+timedelta(hours=3)) < value['end']:
                cheaters_list.append(name)
   
    return cheaters_list

if __name__ == "__main__":
    print(cheaters())