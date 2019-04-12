import random
from datetime import datetime
import time
import sys

#Amount of items to add to the list to sort
itemCount = 10

#Amount of times to simulate sorting the list


#List that is used to store data that is sorted
list_of_variables = []

#Generate the data and randomize it
def initList():
    for x in range(itemCount):
        list_of_variables.append(x+1)
    random.shuffle(list_of_variables)

'''
This function takes the input of a list and it will sort that list in the order of lowest to highest. It works by choosing
a start value and an end value(the beginning and the end of the list) and finds the largest value within that interval, then the
interval is updated by increasing the start value and this process is continued through the list until the list is sorted.
*However it is important to note that this function is just the big picture and the actual sorting takes place in moveLargest()
'''
def quickSort(sortList):
    end = len(sortList)
    start = 0
    while start != end:
        start = moveLargest(sortList,start,end)


'''
This function is what does the actual sorting of the algorithm.
It takes 3 inputs the list to be sorted, the start of the interval to sort over, and the end of the interval.
It loops over the interval and chooses the largest number from said iterval and swaps the largest number with the largest number
in the interval.
'''
def moveLargest(sortList, start, end):
    currentMax = -10000;
    for item in range(start,len(sortList)):
        if (sortList[item] > currentMax):
            currentMax = sortList[item]
    swapIndex(sortList, start, sortList.index(currentMax))
    start += 1
    return start

'''
This function takes in 3 inputs, the list that is being sorted, the first index to switch and the second index to switch
The two index will be switched in the list entered
'''
def swapIndex(list, index1, index2):
    tempVal = list[index1]
    list[index1] = list[index2]
    list[index2] = tempVal

def displayList(list):
    for x in list:
        print('*'*x)
        # print("\n")

initList()
displayList(list_of_variables)
# print(list_of_variables)
print('-'*10)
quickSort(list_of_variables)
displayList(list_of_variables)
# print(list_of_variables)