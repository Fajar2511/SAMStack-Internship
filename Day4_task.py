print("Day 4 Tasks:")
print("Task 1: Division of two numbers with error handling")

def divide(a, b):
    try:
        result = a / b
        print("Division successful:", result)
    except ZeroDivisionError:
        print("Error: Division by zero is not possible")

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    divide(num1, num2)
except ValueError:
    print("Error: Please enter only numeric values")

print("\nTask 2: Extracting ID and Email from a structured string")
raw_data = "Name: Fajar | ID: 1024 | Status: Active | Email: fajar@example.com"
Raw_Data = raw_data.split(" | ")
data_dict = {}
for part in Raw_Data:
    key, value = part.split(": ")
    data_dict[key] = value

print("ID:", data_dict["ID"])
print("Email:", data_dict["Email"])
print("Structured Dictionary:", {"ID": data_dict["ID"], "Email": data_dict["Email"]})

print("\nTask 3: Custom Exception for Invalid Semester Input")
class InvalidSemesterError(Exception): 
    pass
def check_semester():
    try:
        s = int(input("Enter semester: "))
        if not 1 <= s <= 8:
            raise InvalidSemesterError("Invalid semester: Please enter a value between 1 and 8.")
        print("Semester:", s)
    except ValueError:
        print("Error: Enter numeric value")
    except InvalidSemesterError as e:
        print("Error:", e)

check_semester()