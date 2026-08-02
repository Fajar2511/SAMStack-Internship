print("PART 5: Functions")

num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
def add_numbers(a, b):
    return a + b
result = add_numbers(num1, num2)
print("The sum of", num1, "and", num2, "is:", result)
print("To check if a number is prime:")
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
print("To Demostrate arguments:")
def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")
greet("Alice", 30)
def print_values(*args):
    for arg in args:
        print(arg)
print_values("Hello", "World", 1, 2, 3)
def print_key_values(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)  
print_key_values(name="Alice", age=30, city="New York")
