print("PART 10: Exception Handling")

try:
    num = int(input("Enter a number: ")) 
    file = open("data.txt", "r") 
    data = file.read()
    print(100 / num) 
    print(data[10]) 

except ValueError:
    print("Error: Invalid input. Please enter an integer.")

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except FileNotFoundError:
    print("Error: File not found.")

except IndexError:
    print("Error: Index out of range.")

except Exception as e:
    print("An unexpected error occurred:", e)

else:
    print("No error occurred. Code ran successfully.")
