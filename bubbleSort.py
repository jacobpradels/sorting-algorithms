import random
from datetime import datetime

#Amount of items to add to the list to sort
iterationCount = 15

#Variable used to track processing time
startTime = datetime.now()

#List that is used to store data that is sorted
list_of_variables = []

#Generate the data
def initList():
    for x in range(iterationCount):
        list_of_variables.append('*'*(x+1))

#Display the data formatted
def displayList(inputList):
    for x in range(len(inputList)):
        print(inputList[x])

#Apply the bubble sort algorithm
def sortList(inputList):
    for x in range(len(inputList)):
        if x != len(inputList)-1:
            if (len(inputList[x]) < len(inputList[x+1])):
                tempVar = inputList[x]
                inputList[x] = inputList[x+1]
                inputList[x+1] = tempVar

#Function for iterating the sorting algorithm n times
def repeatMainLoop(n):
    for x in range(n):
        sortList(list_of_variables)

#Function to determine if the list has been successfully sorted
def checkSorted(inputList):
    sorted = True
    for x in range(len(inputList)):
        if x != len(inputList)-1:
            if (len(inputList[x]) < len(inputList[x+1])):
                sorted = False
    return sorted

#Main Function
def main():
    initList()
    random.shuffle(list_of_variables)
    displayList(list_of_variables)
    print('-'*15)
    while (not checkSorted(list_of_variables)):
        sortList(list_of_variables)
    displayList(list_of_variables)
main()

#Determine final execution time and display it
endTime = str(datetime.now() - startTime)
print("executed in " + endTime[6:len(endTime) - 1] + " seconds")
