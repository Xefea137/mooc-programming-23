# Write your solution here
def older_people(people: list, year: int):
    name = []
    for item in people:
        if item[1] < year:
            name.append(item[0])
    return name

if __name__ == "__main__":
    p1 = ("Adam", 1977)
    p2 = ("Ellen", 1985)
    p3 = ("Mary", 1953)
    p4 = ("Ernest", 1997)
    people = [p1, p2, p3, p4]
    older = older_people(people, 1979)
    print(older)