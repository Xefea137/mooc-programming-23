# WRITE YOUR SOLUTION HERE:
class ListHelper:
    @classmethod
    def make_dictionary(cls, my_list: list):
        number_dictionary = {}
        for item in my_list:
            if item in number_dictionary:
                number_dictionary[item] += 1
            else:
                number_dictionary[item] = 1

        return number_dictionary

    @classmethod
    def greatest_frequency(cls, my_list: list):
        number_dictionary = ListHelper.make_dictionary(my_list)

        max = 0
        for key, value in number_dictionary.items():
            if value > max:
                max = value
                name = key
        
        return name

    @classmethod  
    def doubles(cls, my_list: list):
        number_dictionary = ListHelper.make_dictionary(my_list)

        double = 0
        for value in number_dictionary.values():
            if value >= 2:
                double += 1

        return double

if __name__ == "__main__":
    #numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
    numbers = [1, 1, 1, 2, 2, 3]      
    print(ListHelper.greatest_frequency(numbers))       
    print(ListHelper.doubles(numbers))                  