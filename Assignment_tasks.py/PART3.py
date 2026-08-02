print("\nPART 3:Control Statements:")

print("To check if a number is positive, negative, or zero:")
n=int(input("Enter a number: "))
if n>0:
    print("Positive number")            
elif n<0:
    print("Negative number")
else:
    print("Zero")   
print("Grading System:")
grade=int(input("Enter your grade (0-100): "))
if grade>=90:
    print("Grade: A")
elif grade>=80:
    print("Grade: B")
elif grade>=70:
    print("Grade: C")
elif grade>=60:
    print("Grade: D")   
else:
    print("Grade: F")
