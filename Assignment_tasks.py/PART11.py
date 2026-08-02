print("PART 11: Object-Oriented Programming")

class Student:
    def __init__(self, input_name, input_age, input_grade):
        self.name = input_name
        self.age = input_age
        self.grade = input_grade
    def display_info(self):
            print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")   
class Teacher(Student):
    def __init__(self, input_name, input_age, input_subject):
        super().__init__(input_name, input_age, None )
        self.subject = input_subject
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Subject: {self.subject}")
student1 = Student("Alice", 20, "A")
student1.display_info()
teacher1 = Teacher("Mr. Smith", 35, "Math")
teacher1.display_info()
