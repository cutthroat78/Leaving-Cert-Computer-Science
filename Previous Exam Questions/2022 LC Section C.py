# Question 16(a)
# Examination Number:
from random import randint

print("Dice simulation and analysis program\n")  # print the string: Dice simulation and analysis program

results = []
frequencies = [0, 0, 0, 0, 0, 0]

# Loop 100 times
for i in range (100):
    throw_result = randint(1,6) # store a random value between 1 and 6
    results.append(throw_result) # append each value to results

# Start to build up a list of frequencies for each value thrown
    if throw_result == 1: # check if variable named throw_result is equal to 1
        frequencies[0] = frequencies[0] + 1
    elif throw_result == 2: # check if variable named throw_result is equal to 2
        frequencies[1] = frequencies[1] + 1
    elif throw_result == 3: # check if variable named throw_result is equal to 3
        frequencies[2] = frequencies[2] + 1
    elif throw_result == 4: # check if variable named throw_result is equal to 4
        frequencies[3] = frequencies[3] + 1
    elif throw_result == 5: # check if variable named throw_result is equal to 5
        frequencies[4] = frequencies[4] + 1
    elif throw_result == 6: # check if variable named throw_result is equal to 6
        frequencies[5] = frequencies[5] + 1

#print("Results:", results)
print("Frequencies:", frequencies)
print("Dice Frequency\n---- ----------\n", "1", "     ", frequencies[0], "\n", "2", "     ", frequencies[1], "\n", "3", "     ", frequencies[2], "\n", "4", "     ", frequencies[3], "\n", "5", "     ", frequencies[4], "\n", "6", "     ", frequencies[5], "\n")