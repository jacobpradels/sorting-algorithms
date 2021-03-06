import random
from datetime import datetime
import time
import sys
'''
Bubblesort is inefficient and this was made for practice and demonstration only
'''
#Amount of items to add to the list to sort
itemCount = 5

#Amount of times to simulate sorting the list
dataSetCount = 100

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

#Function to swap the indexes of two items
def swapIndex(x,g,inputList):
    tempVar = inputList[x]
    inputList[x] = inputList[g]
    inputList[g] = tempVar

#Display the data formatted
def displayList(inputList):
    for x in range(len(inputList)):
        print(inputList[x])

#Apply the bubble sort algorithm
def sortList(inputList):
    global stepsTaken;
    for x in range(len(inputList)):
        if x != len(inputList)-1 and (inputList[x] < inputList[x+1]):
            swapIndex(x,x+1,inputList)


#Function for iterating the sorting algorithm n times
def repeatMainLoop(n):
    for x in range(n):
        sortList(list_of_variables)

#Function to determine if the list has been successfully sorted
def checkSorted(inputList):
    sorted = True
    for x in range(len(inputList)):
        if x != len(inputList)-1 and (inputList[x] < inputList[x+1]):
            sorted = False
    return sorted

#Main Function
def main():
    #Variables for data collection
    startTime = datetime.now()
    stepsTaken = 0

    #Generate a new list for every iteration of main
    initList()
    #continue this loop until the list has been sorted
    while (not checkSorted(list_of_variables)):
        sortList(list_of_variables)
        stepsTaken += 1

    #collect the data after the sorting is completed
    endTime = str(datetime.now() - startTime)
    dataDictionary["Time"] += float(endTime[6:len(endTime)-1])
    dataDictionary["Steps"] += stepsTaken


#Progress bar is there to show program hasn't crashed, however it doesn't have a specified length
print('Starting... \n')
progressBarChange = dataSetCount / 100
progressBarProgress = 0;

#Repeat the main function as dataSetCount amount of times
for x in range(dataSetCount):
    main()
    progressBarProgress += progressBarChange
    if (progressBarProgress > progressBarChange):
        progressBarProgress = 0
        sys.stdout.write("-")
        sys.stdout.flush()
sys.stdout.write("\n")
print('done.')

#Calculate average steps
dataDictionary["Average Steps"] = dataDictionary["Steps"]/dataSetCount


#Output this info to a text document for comparison
textPad = open("results.txt", "a+")
textPad.write("\nData set for Bubble Sort algorithm over " + str(dataSetCount) + " iterations with " + str(itemCount) + " items.\n")
for key in dataDictionary:
    textPad.write(key + " : " + str(dataDictionary[key]) + "\n")
