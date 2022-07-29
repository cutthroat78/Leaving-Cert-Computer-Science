# Question 16(a)
# Name and School: Matthew Renehan, Clogher Road Community College
import random # Imports random module

while True:
    s_name=input("Enter your surname:      ") # User inputs surname
    f_name=input("Enter your first name:      ") # User inputs first name
    age=int(input("Enter your age:      ")) # User inputs age
    trail=input("Do you agree to enrol in a vaccine trial?\nType 'Yes' or 'No'      ") # User inputs if they want to be in a vaccine trail
    trailvaccines=["A","B","C"] # List of vaccines for if the user decides to enrol in a vaccine trial
    eircode=input("Enter your Eircode:      ") # User inputs eircode
    print("Hello", f_name, s_name, "you are", age, "years old and your Eircode is", eircode) # Displays user information that was inputed
    if int(eircode[-1]) % 2 != 0: # Checks if eircode ends with an odd number
        print("You must attend Northfield for your vaccine")
    elif int(eircode[-1]) % 2 == 0: # Checks if eircode ends with an even number
        print("You must attend Eastwood for your vaccine")
    if trail == "Yes": # Checks if trail option answer is "Yes"
        print("You are not enrolled in the trail to receive Super vaccine", random.choice(trailvaccines))
    elif trail == "No": # Checks if trail option answer is "No"
        if age < 12: # Checks if age is below 12
            print(f_name, "You are too young to get a vaccine")
        elif age >= 12 and age <= 49:  # Checks if age is between 12 and 49
            print(f_name, "You will receive the MRNA vaccine")
        elif age > 49: # Checks if age is above 49
            print(f_name, "You will receive the ADENO vaccine")
    option=input("If you have finished entering people's details type 'END', other press RETURN:      ") # Ask user if they have finished entering details
    if option == "END": # Checks if option is the string "END"
        break # Stops the programs
    else:
        continue # Starts from the start of the loop