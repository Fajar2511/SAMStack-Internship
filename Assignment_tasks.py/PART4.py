print("PART 4:Loops And Iterations:")

print("To print numbers from 1 to 20:")
for i in range(1,21):
    print(i)
print("To print even numbers from while loop:")
while True:
    num=int(input("Enter a number: "))
    if num%2==0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
    cont=input("Do you want to continue? (y/n): ")
    if cont.lower()!="y":
        break
print("Multiplication Table using Nested Loop\n")

for i in range(1, 11): 
    for j in range(1, 11):
        print(i, "x", j, "=", i * j)
    print() 