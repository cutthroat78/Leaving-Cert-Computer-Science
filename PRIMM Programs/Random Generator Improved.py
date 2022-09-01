#Name:
#Purpose: To create a random name generator
#Date:

# identify and import the libraries we want to use
import random
import csv

#identify the file by name and tell the program to read the data
File = open("adjectives.csv", "r")
importedData = File.read()
File.close

#Split the imported data wherever it finds a comma and store as a list
adjectivesList = importedData.split(",") 

#1. Open the file animalNames.csv adn read it into this program
File = open("animalNames.csv", "r")
importedData = File.read()
File.close

#2. Split the imported aimal Names and save it as a new list
animalNamesList = importedData.split(",") 

#Find the maximum number of items in the list and store it as a variable
maxAdjectivesNumber = len(adjectivesList)-1
rAdjectivesLoc = random.randint(0, maxAdjectivesNumber)


#3. Pick a new random number that is contained within the new list and save it as a new variable called rAnimalNamesLoc.
maxAnimalNamesNumber = len(animalNamesList)-1
rAnimalNamesLoc = random.randint(0, maxAnimalNamesNumber)


#4. Concatenate the new random animal name onto the userName.
userName = ("".join([adjectivesList[rAdjectivesLoc],animalNamesList[rAnimalNamesLoc]]))


print(userName)

#5. Currently the adjectives are all lowercase.#
#Alter the program so that the adjective in the username is capitalised.
