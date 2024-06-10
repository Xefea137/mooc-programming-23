# Tee ratkaisusi tähän:
class DecreasingCounter:
    def __init__(self, initial_value: int):
        self.value = initial_value
        self.reset = initial_value

    def print_value(self):
        print("value:", self.value)

    def decrease(self):
        if self.value > 0:
            self.value -= 1

    # Write the rest of the methods here!
    def set_to_zero(self):
        self.value = 0

    def reset_original_value(self):
        self.value = self.reset

if __name__ == "__main__":
    '''counter = DecreasingCounter(10)
    counter.print_value()
    counter.decrease()
    counter.print_value()
    counter.decrease()
    counter.print_value()
    #value: 10
    #value: 9
    #value: 8'''

    '''counter = DecreasingCounter(2)
    counter.print_value()
    counter.decrease()
    counter.print_value()
    counter.decrease()
    counter.print_value()
    counter.decrease()
    counter.print_value()
    #value: 2
    #value: 1
    #value: 0
    #value: 0'''

    '''counter = DecreasingCounter(100)
    counter.print_value()
    counter.set_to_zero()
    counter.print_value()
    #value: 100
    #value: 0'''

    counter = DecreasingCounter(55)
    counter.decrease()
    counter.decrease()
    counter.decrease()
    counter.decrease()
    counter.print_value()
    counter.reset_original_value()
    counter.print_value()
    #value: 51
    #value: 55