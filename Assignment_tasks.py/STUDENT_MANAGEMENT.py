print("PART 12: Student Management System")

FILENAME = "students.txt"
class Student:
    def __init__(self, roll, name, grade):
        self.roll = roll
        self.name = name
        self.grade = grade

students = []

def load():
    global students
    try:
        with open(FILENAME, "r") as f:
            for line in f:
                r, n, g = line.strip().split(",")
                students.append(Student(r, n, g))
    except:
        pass

def save():
    with open(FILENAME, "w") as f:
        for s in students:
            f.write(f"{s.roll},{s.name},{s.grade}\n")

def add():
    r = input("Roll: ")
    n = input("Name: ")
    g = input("Grade: ")
    students.append(Student(r, n, g))
    save()
    print("Added!")

def view():
    if len(students) == 0:
        print("No data")
    for s in students:
        print(s.roll, s.name, s.grade)

def update():
    r = input("Roll to update: ")
    for s in students:
        if s.roll == r:
            s.name = input("New Name: ")
            s.grade = input("New Grade: ")
            save()
            print("Updated")
            return
    print("Not found")

def delete():
    r = input("Roll to delete: ")
    for s in students:
        if s.roll == r:
            students.remove(s)
            save()
            print("Deleted")
            return
    print("Not found")

load()
while True:
    print("\n1.Add 2.View 3.Update 4.Delete 5.Exit")
    ch = input("Choice: ")
    
    if ch == "1": add()
    elif ch == "2": view()
    elif ch == "3": update()
    elif ch == "4": delete()
    elif ch == "5": 
        print("Bye")
        break
    
    