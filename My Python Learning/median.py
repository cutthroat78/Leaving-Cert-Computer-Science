#!/usr/bin/python3

my_list = [] # defines a empty list
while True: # make a infinite loop
    number = input("Input a number for the list, type q to quit inputting numbers\n") # ask the user for a number and set that number to the variable named variable
    if number == "q": # if variable named number is q
        break # break the infinite loop
    else: # if it is not q
        my_list.append(int(number)) # convert the string variable named number to an integer and append it to the list called my_list

if (len(my_list) % 2) == 0:
    middle = len(my_list)/2
    middle1 = my_list[int(middle)].sort
    middle2 = my_list[int(middle)+1].sort
    print(int(middle1) + int(middle2) / 2)
else:
     print("To be done")
