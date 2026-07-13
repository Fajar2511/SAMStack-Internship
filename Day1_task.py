print("Day 1 Tasks")
print("Task 1: ")

name = input("Enter your name: ")
semester = int(input("Enter your Semester: "))
GPA = float(input("Enter your GPA: "))
print(f"Hello {name}, you are in semester {semester} with GPA {GPA}.")
print("Type of name:", type(name))
print("Type of semester:", type(semester))
print("Type of GPA:", type(GPA))

print("Task 2: ")

intlist=[1,6,2,3,8,9,12,14,15,11]
evenlist=[]
oddlist=[]
for i in range(0,len(intlist)):
     if intlist[i]%2==0:
        evenlist.append(intlist[i])
for j in range(0,len(intlist)):
    if intlist[j]%2!=0:
       oddlist.append(intlist[j])
       
print("Even list:",evenlist)
 
print("Odd list:",oddlist)

print("Task 3: ")

num = int(input("Enter a number: ")) 
def isprime(num): 
    if num <= 1: 
        print("num is not prime")
        return False
    for i in range(2, num):
        if num % i == 0: 
        
            print("it is not prime")
            return False
    
    print("it is a prime number")
    return True

print(isprime(num))