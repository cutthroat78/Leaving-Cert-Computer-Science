#Question 16 (b)
#Student name: 
import random # Import the python library named random
ticket = [] # Define an empty list called ticket

def pick_number(num): # Define a function called pick_number that takes in one input and stores that input as a variabled called num
    times = 0 # define a variable called times and set it to 0
    while True: # start an infinite loop that needs to broken with the "break" function to leave it
        if times == num: # check if times variable is equal to the variabled called num. This is to check how many times the infinite loop ran for
            break # break/stop the infinite loop
        else: # if times variable doesn't equal the variable called num then run the below lines
            user_number = int(input ("Please pick a number between 1 and 10: ")) # ask the user to pick a number between 1 and 10 and store it as a variable called user_number
            ticket.append(user_number) # append value of variable named user_number to the list called ticket
            times += 1 # add one to the value of variable named times
            
pick_number(3) # run the function called pick_number with the input of 3 (for it to run the user picking their numbers code three times)

print ("Your ticket is: ", ticket) # print the string "Your ticket is: " and the value of the variable called ticket after it 

print ("The draw will start now, good luck!") # print the string "The draw will start now, good luck!"


drum = [1,2,3,4,5,6,7,8,9,10] # define a list called drum that has the contents 10 items, which are the numbers from 1 to 10
result = [] # Define an empty list called result

def lotto(num): # Define a function called lotto that takes in one input and stores that input as a variabled called num
    times = 0 # define a variable called times and set it to 0
    while True: # start an infinite loop that needs to broken with the "break" function to leave it
        if times == num: # check if times variable is equal to the variabled called num. This is to check how many times the infinite loop ran for
            break # break/stop the infinite loop
        else: # if times variable doesn't equal the variable called num then run the below lines
            draw = drum[random.randint(0,len (drum))-1] # pick a random number from the list called drum and store it as a variable called draw
            if result.count(draw) == 1: # check if the value of the variable named draw already exists in the list called result and run below line of code if the value of the variable named draw already exists in the list called result
                continue # go back to the start of the infinite loop
            result.append(draw) # append value of variable named draw to the list called result
            times += 1 # add one to the value of the variable named times
    print("The draw was: ", result) # print the string "The draw was: " and the values of the list called result after it

lotto(3) # run the function called lotto with the input of 3 (for it to run the user picking their numbers code three times)

check_result = result[0] + result[1] + result[2] # add up the first, second and third items of the list called result

check_ticket = ticket[0] + ticket[1] + ticket[2] # add up the first, second and third items of the list called ticket

if check_result == check_ticket: # check if value of variable called check_result and value of variable called check_ticket are the same value, if they are the same run the below line of code
    print("You win!") # print the string "You win!"
else: # if the value of variable called check_result and the value of variable called check_ticket are not the same value, run the below line of code
    print("You lose!") # print the string "You lose!"
