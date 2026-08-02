print("PART 7: Dictionaries and Data Handling")

student_Dict = {
    "name": "John",
    "age": 20,
    "grade": "A"
}
print("Student Dictionary:", student_Dict)
print("Value Access and Update of Student Dictionary:")
student_Dict["age"] = 21
student_Dict["name"] = "Fajar"
student_Dict["grade"] = "B"
for item in student_Dict.items():
    print(item)
