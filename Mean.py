# Program to find the mean of a list of values
# Version 1
# Calculate and return the mean of all the values in L
def arithmetic_mean(L):  # set the initial value of total to zero (function)
    total = 0
     # running total of values in L
     # Now loop over the list
    for v in L:
        total = total + v
    return total/len(L) 
# Divide by the total by the number of values in L
# PYTHON STARTS EXECUTING FROM HERE ...
# Initialise a list of values
my_list = [] # defines a empty list
while True: # make a infinite loop
    number = input("Input a number for the list, type q to quit inputting numbers\n") # ask the user for a number and set that number to the variable named variable
    if number == "q": # if variable named number is q
        break # break the infinite loop
    else: # if it is not q
        my_list.append(int(number)) # convert the string variable named number to an integer and append it to the list called my_list
# Call the function
my_mean = arithmetic_mean(my_list)
# Display the answer
print("The mean is ", my_mean)
