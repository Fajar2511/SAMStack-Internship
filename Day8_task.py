class Student:
    
    def __init__(self, name, roll_number, grades):
        self.name = name
        self.roll_number = roll_number
        self.grades = grades  

    
    def calculate_gpa(self):
        if len(self.grades) == 0:
            return 0.0
        return sum(self.grades) / len(self.grades)

    
    def display_profile(self):
        gpa = self.calculate_gpa()
        
        print(f"Name       : {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print(f"GPA        : {gpa:.2f}")  
        

    
    def __str__(self):
        return f"Student(Name: {self.name}, Roll No: {self.roll_number})"


student1 = Student("Ayesha Khan", 101, [90, 85, 92, 88])
student2 = Student("Ali Raza", 102, [75, 80, 78, 82])
student3 = Student("Fatima Noor", 103, [95, 98, 94, 96])


print(student1)
print(student2)
print(student3)
print("\n")


student1.display_profile()
student2.display_profile()
student3.display_profile()