# Write your solution here
import re
def is_dotw(my_string: str):
    return True if re.search("Mon|Tue|Wed|Thu|Fri|Sat|Sun", my_string) else False

def all_vowels(my_string: str):
    return False if re.search("[^aeiou]", my_string) else True
    #return re.search("^[aeiou]*$", my_string) is not None

def time_of_day(my_string: str):
    return True if re.search("^([0-1][0-9]|[2][0-4]):[0-5][0-9]:[0-5][0-9]$", my_string) else False

if __name__ == "__main__":
    print(time_of_day("12:43:01"))
    print(time_of_day("AB:01:CD"))
    print(time_of_day("17:59:59"))
    print(time_of_day("33:66:77"))
    print(time_of_day("25:13:01"))
    print(time_of_day("19:zz:04"))