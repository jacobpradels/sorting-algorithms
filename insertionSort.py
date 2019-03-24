import random
from datetime import datetime
import time
import sys

#Amount of items to add to the list to sort
itemCount = 5

#Amount of times to simulate sorting the list
dataSetCount = 48
#Accumulator for the amount of changes made

toolbar_width = 50
global dataDictionary
dataDictionary = {"Steps":0,"Time":0}



#List that is used to store data that is sorted
list_of_variables = []

#Generate the data and randomize it

def initList():
    for x in range(itemCount):
        list_of_variables.append(x+1)
    random.shuffle(list_of_variables)


#Display the data formatted
def displayList(inputList):
    for x in range(len(inputList)):
        print(inputList[x])

#Function to swap the indexes of two items
def swapIndex(x,g,inputList):
    tempVar = inputList[x]
    inputList[x] = inputList[g]
    inputList[g] = tempVar

#Algorithm for sorting the list
def sortList(inputList):
    for x in range(len(inputList)):
        if x < len(inputList)-1:
            if (inputList[x] > inputList[x+1]):
                #print(inputList[x],inputList[x+1])
                swapIndex(x,x+1,inputList)

#Check if the list has been successfully sorted
def checkSorted(inputList):
    sorted = True
    for x in range(len(inputList)):
        if x != len(inputList)-1 and inputList[x] > inputList[x+1]:
            sorted = False
    return sorted


def main():
    #Variables for data collection
    global dataDictionary
    startTime = datetime.now()
    stepsTaken = 0

    #New List for every iteration of main
    initList()

    #Continue the loop until the list is sorted
    while (not checkSorted(list_of_variables)):
        sortList(list_of_variables)
        stepsTaken += 1

    #collect the data after iterations
    endTime = str(datetime.now() - startTime)
    dataDictionary["Time"] += float(endTime[6:len(endTime)-1])
    dataDictionary["Steps"] += stepsTaken

#Progress bar is there to show program hasn't crashed, however it doesn't have a specified length
print('Starting... \n')
progressBarChange = float(dataSetCount) / 100
progressBarProgress = 0;

#Repeat the main function while updating the progress bar
for x in range(dataSetCount):
    main()
    progressBarProgress += progressBarChange
    if (progressBarProgress > progressBarChange):
        progressBarProgress = 0
        sys.stdout.write("-")
        sys.stdout.flush()
sys.stdout.write("\n")
print('done.')
#Calculate the average steps
dataDictionary["Average Steps"] = dataDictionary["Steps"]/dataSetCount

#Output the results to a text document for comparison
textPad = open("results.txt", "a+")
textPad.write("\nData set for Insertion Sort algorithm over " + str(dataSetCount) + " iterations with " + str(itemCount) + " items.\n")
for key in dataDictionary:
    textPad.write(key + " : " + str(dataDictionary[key]) + "\n")
