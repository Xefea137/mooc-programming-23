# Write your solution here
def create_tuple(x: int, y: int, z: int):
    list1 = [x,y,z]
    tuple1 = (min(list1),max(list1),sum(list1))
    return tuple1

if __name__ == "__main__":
    print(create_tuple(5, 3, -1))
    #print(create_tuple(1, 4, 2))