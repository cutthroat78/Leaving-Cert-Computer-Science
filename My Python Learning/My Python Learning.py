# Hello World
print("Hello World")

# Double Print
print("Line 1")
print("Line 2")

# Print with Tabs Not using Tab Key
print("Hello\tWorld\tI love the weather")

# Two Lines with One Print
print("Hello World\nI love the weather")

# Print Number 22
print(22)

# Add 10 to 10
print(10 + 10)

# Making a Comment
#this is a comment

# Comment with Code
print(10 + 10) # Add 10 + 10 nv  hh

# Using Multi Line Comments
"""
This is a Multi Line Comments
This is a second line
This is a third line
"""

# Making a Variable
x = 4

# Using a Variable in Maths with Print
x = 4
print(x+10)

# Using Two Variables in Maths with Print
x = 4
y = 6
print(x + y)

# Making a Variable using a Name and Use in a Print
John = 7
print(John)

# Putting a String in a Variable and Use in a Print
Your_Name = "Matthew"
print(Your_Name)

# Print an integer
print(int(3))

# Print a float
print(float(8.9))

# Convert a float to integer
x = 8.909
print(int(x))

# Print a string
print(str(8))

# Convert number to boolean
x = 1
y = 0
print(bool(x))
print(bool(y))

# Setting different variables and using type() to get Python to tell us what each variable's type is

a = 8.37
b = "Matthew"
c = 10
d = True 

print(type(a))
print(type(b))
print(type(c))
print(type(d))

# Print all variables in above example using one print function
print(type(a),type(b), type(c), type(d))

# Defining two variables in one line (And these variables will be used in below examples)
x,y = 3,2

# Using + (Add) Operation
print(x+y)

# Using - (Subtract) Operation
print(x-y)

# Using * Operation
print(x*y)

# Using / (Float Division) Operation
print(x/y)

# Using // (Integer Division) Operation
print(x//y)

# Making a program that calculates the volume of a sphere
pi = 3.14 # what we picked as pi
r = 5 # radius we choose (we can vary)

answer = ((4/3*pi)*r**3) # ** is a power

round_ans = round(answer,1)
print(round_ans)

# My version of a program that calculates the volume of a sphere
pi = 3.14
r = input("What is your Radius?")

r = float(r)

answer = ((4/3*pi)*r**3)

print(answer)
option = input("Do you want to round it?")
if option == "yes":
    print(round(answer,1))
elif option == "no":
    print("Done!")
else:
    print("Type yes or no next time")

# Making a program that calculates the volume of a cone
pi = 3.14
r = input("What is your Radius?")
h = input("What is your Height?")

r = float(r)
h = float(h)

answer = ((1/3*pi)*r**2*h)

print(answer)
option = input("Do you want to round it?")
if option == "yes":
    print(round(answer,1))
elif option == "no":
    print("Done!")
else:
    print("Type yes or no next time")

# Using input()
print("What is your name?") # Question on Output
name = input() # Defines the input (typed name)
print("Good Morning",name,"What is your PPS Number?") # Print strings and name variable

# Shortening input() program
name = input("What is your name?") # Take input and make the input a variable
print("Good Morning",name,"What is your PPS Number?") # Print strings and name variable

# Inputing Variables
age = int(input("What is your age?")) # Take input and convert it to an integer
print("I am",age,"years old") # Print strings and age variable

# Inputing Variables with \n in input
age = int(input("What is your age?\n")) # Take input and convert it to an integer
print("I am",age,"years old") # Print strings and age variable

# Chapter 1 Page 18 Question 2
num1 = 5.3
num2 = 9.4
print("Numbers:")
print(num1, num2)
print("Sum:")
print(num1 + num2)
print("Difference:")
print(num1 - num2)
print("Product:")
print(num1 * num2)

# Chapter 1 Page 18 Question 3
x=6.557
y=8.434
sum=(x+y)/2
print("The Average is:",sum)
print("Rounded:", round(sum, 2))
print(x, "to the power of", y, "is", round(x**y))

# Chapter 1 Page 19 Question 4
temp = int(input("What temperature in Fahrenheit is it?\n"))
print("The Temperature in Celcius is:", round((5/9)*(temp-32)))

# Chapter 1 Page 19 Question 8
houselength = 30
housewidth = 10
gardenlength = 40
gardenwidth = 20
gardenarea = gardenlength*gardenwidth
housearea = houselength*housewidth
areatomow = gardenarea-housearea
print("The Area of the Garden is:", areatomow,"m²", "\nIt would take",round(((areatomow/2)/60),2), "minutes to cut the grass")

# Using Boolean 
true = True
print(true)

# Boolean Using Our Ages
Megan = 16
Cathal = 16
Iustina = 17
Matthew = 17
Aine = 35
print(Aine > Cathal)
print(Megan < Aine)
print(Matthew > Iustina)
print(Matthew >= Iustina)
print(Cathal != Megan)

# My version of above code
Cathal, Megan, Iustina, Matthew, Aine = 16, 16, 17, 17, 35
print(Aine > Cathal, Megan < Aine, Matthew > Iustina, Matthew >= Iustina, Cathal != Megan)

# More Boolean Logic 
Megan = 16
Cathal = 16
Iustina = 17
Matthew = 17
Aine = 35
one = (Cathal > Aine) #False
two = (Aine > Cathal) #this answer is True
three = (Matthew > Iustina) #False
four = (Matthew >= Iustina) #True

print(one and two)
print(two or three)
print(four and not two)
print(two and four)
print(two and not three)
print(one and two and three)
print(one or two or four)
print(three or not one)

# If else statements
answer = input("Do you like Cheese? (Y/N)\n")
if answer == "Y": #Colon (:) makes an indent (In VSCode)
    print("Awesome")
else:
    print("Oh, Ok")

# Done an Exam Paper Question

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

# Main Program
import random # To generate random numbers
print("Select operation.")
print("1.Multiply")
print("2.Divide")
print("3.Add")
print("4.Subtract")
# Take input from the user
choice = input("Enter choice(1,2,3 or 4):")
num1 = random.randint(1,12)
num2 = random.randint(1,12)

if choice == '1':
    print(num1,"*",num2,"=", multiply(num1,num2))
elif choice == '2':
    print(num1,"/",num2,"=", divide(num1,num2))
elif choice == "3":
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == "4":
    print(num1, "-", num2, "=", subtract(num1, num2))
else:
    print("Please type 1,2,3 or 4 as your selection")
