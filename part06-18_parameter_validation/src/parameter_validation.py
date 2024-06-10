# Write your solution here
def new_person(name: str, age: int):
    if age < 0 or age > 150 or len(name) == 0 or len(name.split(" ")) <= 1 or len(name) > 40:
        raise ValueError("Invalid parameters.")
    else:
        return (name, age)
    
if __name__ == "__main__":
    print(new_person("J A",1111))