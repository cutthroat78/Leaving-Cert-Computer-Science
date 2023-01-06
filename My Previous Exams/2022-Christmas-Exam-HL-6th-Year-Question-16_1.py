# Question 16(a)
# Student name:
import random # Import the python library named random

def dice_game(): # definte a function called dice_game
    print ("welcome to my dice game!!") # print the string "welcome to my dice game!!"
    
dice_game() # run the function called dice_game

your_name = input("Please enter your name: ") # print the string "Please enter your name: " and have the user input their name and store that name as the variable called your_name

lucky_number = int(input("Please select a lucky number between 1 and 6: ")) # print the string "Please select a lucky number between 1 and 6: " and have the user input their lucky number and store that lucky number as the variable called lucky_number
computer_die_roll = random.randint(1,6) #initialize computer number

print(your_name + "'s lucky number was: " + str(lucky_number)) # print the value of the variable called your_name, then print the string "'s lucky number was: ", then convert the value of the variable called lucky_number to a string and print that string
print("The computer rolled: ", computer_die_roll) # print the string "The computer rolled: " and then print the value of the variable called computer_die_roll

if computer_die_roll == lucky_number: # check if the value of the variable named computer_die_roll and the value of the variable named lucky_number are the same and if so run the below line of code
    print("You guessed correct, well done!") # print the string "You guessed correct, well done!"
elif computer_die_roll < lucky_number: # check if the value of the variable named computer_die_roll is less than the value of the variable named lucky_number and if so run the below line of code
    print("You guessed too high!") # print the string "You guessed too high!"
elif computer_die_roll > lucky_number: # check if the value of the variable named computer_die_roll is greater than the value of the variable named lucky_number and if so run the below line of code
    print("You guessed too low!") # print the string "You guessed too low!"
