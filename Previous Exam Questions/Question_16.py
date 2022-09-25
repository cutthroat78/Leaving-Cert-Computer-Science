# Done an Exam Paper Questions

# Question 16(b)
# # Examination Number:

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def square(x, y):
    return x ** y
# Main Program
import random # To generate random numbers
print("Select operation.")
print("1.Multiply")
print("2.Divide")
print("3.Add")
print("4.Subtract")
print("5.Squaring")
# Take input from the user
choice = input("Enter choice(1,2,3,4 or 5):")
num1 = int(input("What is your first number?"))
num2 = int(input("What is your second number?"))

if choice == '1':
    print(num1,"*",num2,"=", multiply(num1,num2))
elif choice == '2':
    print(num1,"/",num2,"=", divide(num1,num2))
elif choice == "3":
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == "4":
    print(num1, "-", num2, "=", subtract(num1, num2))
elif choice == "5":
    print(num1, "-", num2, "=", square(num1, num2))
else:
    print("Please type 1,2,3 or 4 as your selection")
