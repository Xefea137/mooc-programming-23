# Write your solution here:
class Task:
    id = 1
    
    def __init__(self, description: str, programmer: str, workload: int):
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self.__tast_finished = False
        self.id = Task.id
        Task.id += 1

    def is_finished(self):
        return self.__tast_finished
    
    def mark_finished(self):
        self.__tast_finished = True

    def __str__(self):
        if self.is_finished():
            return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} FINISHED"
        else:
            return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} NOT FINISHED"

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
            
        finished_task = 0
        finished_workload = 0
        unfinished_task = 0
        unfinished_workload = 0
        for item in self.finished_orders():
            if item.programmer == programmer:
                finished_workload += item.workload
                finished_task += 1

        for item in self.unfinished_orders():
            if item.programmer == programmer:
                unfinished_workload += item.workload
                unfinished_task += 1

        return (finished_task, unfinished_task, finished_workload, unfinished_workload)
        
if __name__ == "__main__":
    orders = OrderBook()
    orders.add_order("program webstore", "Adele", 10)
    orders.add_order("program mobile app for workload accounting", "Adele", 25)
    orders.add_order("program app for practising mathematics", "Adele", 100)
    orders.add_order("program the next facebook", "Eric", 1000)

    for order in orders.all_orders():
        print(order)

    orders.mark_finished(1)
    orders.mark_finished(2)

    status = orders.status_of_programmer("Adele")
    print(status)