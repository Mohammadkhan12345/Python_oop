class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def team(self):
        if self.team_size == 3:
            print(f"team size is {self.team_size} and it's an average team")
        elif self.team_size > 3:
            print(f"team size is {self.team_size} and it's a large team")
        else:
            print("Small team! team size is less than 3 persons")

    def show_details(self):
        return f"manager name is {self.name} and his salary is {self.salary} and the team size is {self.team_size}"


emp = Employee("Ali", 50000)
mngr = Manager("Ahmed", 60000, 2)

print(mngr.show_details())
mngr.team()
