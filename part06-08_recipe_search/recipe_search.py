# Write your solution here
def all(filename: str):
    d = {}
    collect = []
    with open(filename) as file:
        for item in file:
            item = item.strip()
            if item != "":
                collect.append(item.strip())
            else:
                d[collect[0]] = collect[1:]
                collect = []
        d[collect[0]] = collect[1:]
    return d

def search_by_name(filename: str, word: str):
    d = all(filename)
    searched = []
    for recipe in d:
        if word in recipe.lower():
            searched.append(recipe)
    return searched

def search_by_time(filename: str, prep_time: int):
    d = all(filename)
    found = []
    for recipe, items in d.items():
        if int(items[0]) <= prep_time:
            found.append(f"{recipe}, preparation time {items[0]} min")
    return(found)

def search_by_ingredient(filename: str, ingredient: str):
    d = all(filename)
    found = []
    for recipe, items in d.items():
        if ingredient in items:
            found.append(f"{recipe}, preparation time {items[0]} min")
    return(found)

if __name__ == "__main__":
    found_recipes = search_by_name("recipes2.txt", "oat")
    for recipe in found_recipes:
        print(recipe)
    print()
    found_recipes = search_by_time("recipes1.txt", 20)
    for recipe in found_recipes:
        print(recipe)
    print()
    found_recipes = search_by_ingredient("recipes1.txt", "eggs")
    for recipe in found_recipes:
        print(recipe)