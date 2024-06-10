# Write your solution here
import json

def print_persons(filename: str):
    with open(filename) as file:
        data = file.read()
        
    course = json.loads(data)
    
    hobbies = ""
    for items in course:
        for item in items['hobbies']:
            hobbies += item + ', '
        print(f"{items['name']} {items['age']} years ({hobbies.rstrip(', ')})")
        hobbies = ""

if __name__ == "__main__":
    print_persons("file1.json")