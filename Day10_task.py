class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_details(self):
        return f"Name: {self.name}, Salary: {self.salary}"

    def work(self):
        print("Employee is performing general duties.")

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)  
        self.programming_language = programming_language

    def work(self):  
        print(f"{self.name} is writing code in {self.programming_language}.")

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)  
        self.team_size = team_size

    def work(self):  
        print(f"{self.name} is managing a team of {self.team_size} developers.")


dev1 = Developer("Fajar", 30000, "Python")
mgr1 = Manager("Eiman", 56000, 5)

employees = [dev1, mgr1]  

for emp in employees:
    print(emp.get_details())
    emp.work()
    print("---")