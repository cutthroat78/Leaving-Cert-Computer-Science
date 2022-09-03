#To take individual letters from a string
myString = "Matthew" # set my name as myString variable
print(myString) # print myString variable
myStringList = list(myString) # set myString as a list
print(myStringList) # print myStringList variable

print(myStringList[1]) # print the first item/letter of myStringList
print(myStringList[6]) # print the first item/letter of myStringList

print(myStringList[2:8]) # print the items/letters of myStringList from (and including) item 2 to 8

if 'a' in (myStringList): # see if item "a" is on myStringList
    print("it is on the list") # print the message if "a" exists in the myStringList list
