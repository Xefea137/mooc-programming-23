# Write your solution here
def list_sum(list1: list, list2: list):
    new_list = []
    for i in range(len(list1)):
        new_list.append(list1[i]+list2[i])
    return new_list

if __name__ == "__main__":
    #a = [1, 2, 3]
    #b = [7, 8, 9]
    #a = [1,2,1,2,1,2]
    #b = [2,3,4,5,6,7]
    a = [-10,-11,-12]
    b = [1,2,3]
    print(list_sum(a, b)) # [8, 10, 12]