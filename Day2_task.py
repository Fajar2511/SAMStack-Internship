print("Day 2 Tasks")
print("task 1:")
text=input("Enter a paragraph: ")
text=text.lower()
text=text.replace(".","").replace(",","")
text=text.split()
freq={}
for word in text:
    if word in freq:
        freq[word]+=1
    else:
        freq[word]=1


print("Word frequencies:")
print(freq)

print("task 2:")
file = open("grade.txt", "w")
 
file.write("Ali,85\n")
file.write("Sara,92\n")
file.write("haris,76\n")
file.write("mohammad,88\n")
file.write("abdullah,64\n")

try:
    file = open("grade.txt", "r")
    total = 0
    count = 0
    for line in file:
        data = line.strip().split(",")
        name = data[0]
        marks = int(data[1])
        total = total + marks
        count = count + 1
    average = total / count
    print("Average Score:", average)
    file.close()
except FileNotFoundError:
    print("File not found.")

print("task 3:")
numbers = [12, 45, 2, 18, 9, 33, 70, 5, 21, 6]
filtered = [num for num in numbers if num > 15 and num % 3 == 0]
print("Original List:", numbers)
print("Filtered List:", filtered)

