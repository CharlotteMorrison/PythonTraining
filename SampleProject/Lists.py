from __future__ import division
import csv

#data definition: ID (numeric), name (string), gender (string),
#eye color (string), race (string), hair color (string),
#height (numeric), publisher (string), skin color (sring),
#alignment (string), weight (numeric)

#create a list to store the data.


def loadHeroes():
    dataset = []
    with open('heroes_information.csv') as dataFile:
        reader = csv.reader(dataFile)
        for row in reader:
            dataset.append(row)
    return dataset


def calculateGenderRatios(dataset):
    maleCount, femaleCount, errorCount = 0,0,0
    for row in dataset:
        if (row[2] == "Male"):
            maleCount+=1
        elif (row[2] == "Female"):
            femaleCount+=1
        else:
            errorCount+=1
    allGender = maleCount + femaleCount + errorCount
    femalePerc= round(femaleCount/allGender * 100.0, 2)
    malePerc = round(maleCount/allGender * 100, 2)

    return femalePerc, malePerc

def tallestHeroes(dataset):


    return


dataset = []
dataset = loadHeroes()

female, male = calculateGenderRatios(dataset)

print(male)
print(female)