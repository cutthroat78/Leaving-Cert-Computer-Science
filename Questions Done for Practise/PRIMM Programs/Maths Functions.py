#Name:
#Date:
#Purpose: To introduce the basics of defining and calling functions

#1. Read the comments and run the code. If you are unsure what it is doing using the debug feature to step through the code.
#2. Change the call of “sub” to use num1 and num2 instead of 6 and 2.
#3. Change num1 and num2 so that the user is asked to input values for them.
#4. Create a new function called “mul” that will multiply num1 and num2 and return the result.
#5. Ask the user to choose between add, sub and mul and use “if” statements to return the value using their chosen function.

def add(a,b): #we define a new function called "add" that takes in two variables
    ans = a + b #we assign a new variable called ans that adds the two variables passed into the function
    return ans #the function returns the new variable defined above

num1 = 6
num2 = 2

print (add(num1,num2)) #we are asking thonny to print the value that is returned from the function "add" when it is passed num1 and num2

def sub(a,b): #we are defining a new function called "sub" that will take in two numbers, subtract them and return the value of the subtraction
    ans = a - b
    return ans

print (sub(6,2))
