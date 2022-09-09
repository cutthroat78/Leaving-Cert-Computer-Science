import random # Import random library
import csv # Import csv library

File = open("/home/cutthroat/work/github/Leaving-Cert-Computer-Science/PRIMM Programs/adjectives.csv", "r") # Open adjectives csv file
importedData = File.read().replace('\n', "") # Read the file and replace any new line with nothing
File.close # close the file

adjectivesList = importedData.split(",") # Have new word start after every ,

File = open("/home/cutthroat/work/github/Leaving-Cert-Computer-Science/PRIMM Programs/animalNames.csv", "r") # Open animalNames csv file
importedData = File.read().replace('\n', "") # Read the file and replace any new line with nothing
File.close # close the file

animalNamesList = importedData.split(",") # Have new word start after every ,

maxAdjectivesNumber = len(adjectivesList)-1 # Get number for how many adjectives there is the csv file
rAdjectivesLoc = random.randint(0, maxAdjectivesNumber) # Pick a random adjective

maxAnimalNamesNumber = len(animalNamesList)-1 # Get number for how many animal names there is in the csv file
rAnimalNamesLoc = random.randint(0, maxAnimalNamesNumber) # Pick a random animal name

numlist =  [ ] # Open an empty list as a var called numlist

for j in range(0,3): # Run next two lines of code three times
    number = random.randint(0,9) # Pick a random number
    numlist.append(number) # Append random number to list var called numlist
    

print(adjectivesList[rAdjectivesLoc] + animalNamesList[rAnimalNamesLoc] + str(numlist[0]) + str(numlist[1]) + str(numlist[2])) # Print adjective, then animalname, then the three random numbers from the list called numlist
