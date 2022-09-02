#Name:
#Purpose: To randomly generate a PIN
#Date:

#Import the necessary library
import random

digit = str(random.randint(0,9))
pin = digit

#1. Use a loop to generate a 5 digit pin stored as a string.
for i in range (1,5):
    digit = str(random.randint(0,9))
    pin = pin+digit
    
print(pin)

#2. Use a loop to generate a 5 digit pin stored as a list
pinList = []
for j in range (0,5):
    digit = random.randint(0,9)
    pinList.append(digit)
    
print(pinList)
