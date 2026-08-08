FILENAME = "grades_data.txt"

def load_students():
    students = []
    try:
        with open(FILENAME, "r") as f:
            for line in f:
                parts = line.strip().split(",")
                students.append(parts)
    except:
        pass
    return students

def save_student(data):
    with open(FILENAME, "a") as f:
        f.write(",".join(data) + "\n")

def get_grade(percentage):
    if percentage >= 90: return "A"
    elif percentage >= 80: return "B"
    elif percentage >= 70: return "C"
    elif percentage >= 50: return "D"
    else: return "F"

def add_student():
    name = input("Enter Name: ")
    roll = input("Enter Roll No: ")

    try:
        m1 = int(input("Enter Maths Marks: "))
        m2 = int(input("Enter Urdu Marks: "))
        m3 = int(input("Enter English Marks: "))
    except:
        print("Error: Marks me number likho")
        return

  
    if m1 < 0 or m1 > 100 or m2 < 0 or m2 > 100 or m3 < 0 or m3 > 100:
        print("Error: Marks 0 se 100 ke beech hone chahiye")
        return

    total = m1 + m2 + m3
    percentage = (total / 300) * 100
    grade = get_grade(percentage)

  
    data = [name, roll, str(m1), str(m2), str(m3), str(total), grade]
    save_student(data)

    print(f"Saved! Total: {total} | %: {percentage:.2f} | Grade: {grade}")

def view_all():
    students = load_students()
    if len(students) == 0:
        print("No records yet")
        return

    print("\nName\tRoll\tM1\tM2\tM3\tTotal\tGrade")
    print("-"*50)
    for s in students:
        print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]}")

def class_report():
    students = load_students()
    if len(students) == 0:
        print("No records yet")
        return

    total_marks = 0
    top = 0
    low = 999
    top_name = ""
    low_name = ""
    failed = []

    for s in students:
        total = int(s[5])
        total_marks += total
        percentage = (total / 300) * 100

        if total > top:
            top = total
            top_name = s[0]
        if total < low:
            low = total
            low_name = s[0]
        if percentage < 50:
            failed.append(s[0])

    average = (total_marks / len(students) / 300) * 100

    print(f"\nClass Average: {average:.2f}%")
    print(f"Top Performer: {top_name} - {top} marks")
    print(f"Lowest Performer: {low_name} - {low} marks")
    print("Students below 50%:", ", ".join(failed) if failed else "None")

def main():
    while True:
        print("\n1. Add Student")
        print("2. View All")
        print("3. Class Report")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_all()
        elif choice == "3":
            class_report()
        elif choice == "4":
            break
        else:
            print("Wrong choice")

main()