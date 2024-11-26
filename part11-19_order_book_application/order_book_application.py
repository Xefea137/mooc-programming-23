# Write your solution here:
class Task:
    id = 0

    @classmethod 
    def new_id(cls):
        Task.id += 1
        return Task.id

    def __init__(self, description: str, programmer: str, workload: int):
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self.tast_finished = False
        self.id = Task.new_id()

    def is_finished(self):
        return self.tast_finished

    def mark_finished(self):
        self.tast_finished = True

    def __str__(self):
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} FINISHED" if self.is_finished() else f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} NOT FINISHED"

class OrderBook:
    def __init__(self):
        self.__work_list = []

    def add_order(self, description, programmer, workload):
        self.__work_list.append(Task(description, programmer, workload))

    def all_orders(self):
        return self.__work_list

    def programmers(self):
        return list(set([item.programmer for item in self.__work_list]))

    def mark_finished(self, id: int):
        for item in self.__work_list:
            if id == item.id:
                item.mark_finished()
                return
        raise ValueError(f"No task with with id {id}")

    def finished_orders(self):
        return ([item for item in self.__work_list if item.is_finished()])

    def unfinished_orders(self):
        return [item for item in self.__work_list if item.is_finished() == False]

    def status_of_programmer(self, programmer: str):

        if programmer not in self.programmers():
            raise ValueError(f"No one named {programmer}")

        finished_task = [item for item in self.finished_orders() if item.programmer == programmer]
        finished_workload = sum(item.workload for item in finished_task)

        unfinished_task = [item for item in self.unfinished_orders() if item.programmer == programmer]
        unfinished_workload = sum(item.workload for item in unfinished_task)

        return (len(finished_task), len(unfinished_task), finished_workload, unfinished_workload)

class OrderBookApplication():
    def __init__(self):
        self.__order = OrderBook()

    def command(self):
        print("commands:")
        print("0 exit")
        print("1 add order")
        print("2 list finished tasks")
        print("3 list unfinished tasks")
        print("4 mark task as finished")
        print("5 programmers")
        print("6 status of programmer")

    def execute(self):
        self.command()
        while True:
            print()
            command = int(input("command: "))
            if command == 0:
                break
            elif command == 1:
                self.add_order()
            elif command == 2:
                self.finished_task()
            elif command == 3:
                self.unfinished_task()
            elif command == 4:
                self.task_finish()
            elif command == 5:
                self.programmers_name()
            elif command == 6:
                self.status()
        
    def add_order(self):
        description = input("description: ")
        programmer_workload = input("programmer and workload estimate: ").split()
        if len(programmer_workload) == 2 and programmer_workload[1].isdigit():
            self.__order.add_order(description, programmer_workload[0], int(programmer_workload[1]))
            print("added!")
        else:
            print("erroneous input")
            return

    def finished_task(self):
        if len(self.__order.finished_orders()) == 0:
            print("no finished tasks")
        for item in self.__order.finished_orders():
            print(item)


    def unfinished_task(self):
        if len(self.__order.unfinished_orders()) == 0:
            print("no unfinished tasks")
        for item in self.__order.unfinished_orders():
            print(item)

    def task_finish(self):
        id = input("id: ")
        try:
            self.__order.mark_finished(int(id))
            print("marked as finished")
        except ValueError:
            print("erroneous input")
            return

    def programmers_name(self):
        for item in self.__order.programmers():
            print(item)

    def status(self):
        name = input("programmer: ")
        try:
            finished, not_finished, done, scheduled = self.__order.status_of_programmer(name)
            print(f"tasks: finished {finished} not finished {not_finished}, hours: done {done} scheduled {scheduled}")
        except ValueError:
            print("erroneous input")
            return
        
order = OrderBookApplication()
order.execute()