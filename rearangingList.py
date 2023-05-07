'''Write a function that receives a list containing the following numbers :
[5, 0, 34, 9, 0, 13, 8]
rearranges the list so that the zeros are the end of the list, and finally returns the arranged list.'''

def rearanging (myList:list) -> list:

    newList = [[num for num in myList if num !=0] +[Zero for Zero in myList if Zero == 0]]

    return newList



myList = [5, 0, 34, 9, 0, 13, 8]

print(rearanging(myList))