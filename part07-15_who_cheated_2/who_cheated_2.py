# Write your solution here
import csv
from datetime import datetime
def final_points():
    cheaters_list = []
    data = {}
    final_score = {}
    
    with open("start_times.csv") as start, open("submissions.csv") as finish:
        for line in csv.reader(start, delimiter=";"):
            data[line[0]] = {"start" : datetime.strptime(line[1], "%H:%M").strftime("%H.%M"), "end" : datetime.strptime(line[1], "%H:%M").strftime("%H.%M"),
             'task' : {'1' : 0, '2' : 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0}}

        for lines in csv.reader(finish, delimiter=";"):
            if (float(datetime.strptime(lines[3], "%H:%M").strftime("%H.%M"))-3) < float(data[lines[0]]['start']) and int(lines[2]) > int(data[lines[0]]['task'][lines[1]]):
                data[lines[0]]['end'] = datetime.strptime(lines[3], "%H:%M").strftime("%H.%M")
                data[lines[0]]['task'][lines[1]] = int(lines[2])

        for name, item in data.items():
            c = 1
            total = 0
            while c < 9:
                total += item['task'][str(c)]
                c += 1
            final_score[name] = total

    return final_score

if __name__ == "__main__":
    print(final_points())