# Write your solution here:
class Clock:
    def __init__(self, hour: int, minute: int, second: int):
        self.seconds = second
        self.minutes = minute
        self.hours = hour

    def tick(self):
        self.seconds += 1
        if self.seconds > 59:
            self.minutes += 1
            self.seconds = 0
            if self.minutes > 59:
                self.hours += 1
                self.minutes = 0
                if self.hours > 23:
                    self.hours = 0

    def set(self, hour: int, minute: int):
        self.hours = hour
        self.minutes = minute
        self.seconds = 0

    def __str__(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"

if __name__ == "__main__":
    clock = Clock(23, 59, 55)
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)

    clock.set(12, 5)
    print(clock)