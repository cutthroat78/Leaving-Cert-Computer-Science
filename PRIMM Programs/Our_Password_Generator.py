import random
import csv

File = open("/home/cutthroat/work/github/Leaving-Cert-Computer-Science/PRIMM Programs/adjectives.csv", "r")
importedData = File.read().replace('\n', "")
File.close

adjectivesList = importedData.split(",") 

File = open("/home/cutthroat/work/github/Leaving-Cert-Computer-Science/PRIMM Programs/animalNames.csv", "r")
importedData = File.read().replace('\n', "")
File.close

animalNamesList = importedData.split(",") 

maxAdjectivesNumber = len(adjectivesList)-1
rAdjectivesLoc = random.randint(0, maxAdjectivesNumber)

maxAnimalNamesNumber = len(animalNamesList)-1
rAnimalNamesLoc = random.randint(0, maxAnimalNamesNumber)

numlist =  [ ]

for j in range(0,3):
    number = random.randint(0,9)
    numlist.append(number)
    

print(adjectivesList[rAdjectivesLoc] + animalNamesList[rAnimalNamesLoc] + str(numlist[0]) + str(numlist[1]) + str(numlist[2]))