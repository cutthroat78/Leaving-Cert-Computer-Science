#Name:
#Purpose: To randomly generate a PIN
#Date:

#Import the necessary library
import random # Import random library

digit = str(random.randint(0,9)) # Pick random number between 0 and 9 and make it digit var
pin = digit # add digit var of number to pin variable

#1. Use a loop to generate a 5 digit pin stored as a string.
for i in range (1,5): # loop next 2 lines of code 5 times
    digit = str(random.randint(0,9)) # Pick random number between 0 and 9 and make it digit var
    pin = pin+digit # Add digit variable to end of pin variable
    
print(pin) # Print pin variable

#2. Use a loop to generate a 5 digit pin stored as a list
pinList = [] # Create empty list var called pinList
for j in range (0,5): # Loop next 2 lines of code 5 times
    digit = random.randint(0,9) # Pick random number between 0 and 9 and make it digit var
    pinList.append(digit) # Append digit to pinList list var
    
print(pinList) # Print pinList variable
