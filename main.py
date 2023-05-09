# --------------- LAB_DICTIONARY ---------------
print("------- Q1 -------")
numberDic = { 
    '0568323222' : "Amal", 
    '0522222232' : "Mohammed", 
    '0532335983' : "Khadijah",
    '0545341144' : "Abdullah",
    '0545534556' : "Rawan",
    '0560664566' : "Faisal", 
    '0567917077' : "Layla",
    '0554096123' : "Suliman"
    }



def checkNum(number):
    '''This fun check if the number is it 10 numbers or not ! '''
    if len(number) != 10 :
        print("This is invalid number!")
    elif not str(number).isdigit():
        print("This is invalid number! 2")
    else:
        return searchOwner(number)

def searchOwner(number):
    '''This fun search about the owner of the number ! '''
    for num in numberDic:
        if number == num:
            result = 1
            owner = num

    if result == 1:
        print(f"Name of owner: {numberDic[owner]} ")
    else:
        print("Sorry, the number is not found !")

'''userInputs = int(input("Enter the phone number: "))
checkNum(userInputs)'''

print("------- Q2 -------")

def arranged(numbers : list ) -> list: 
    arrangedList = []
    for num in numbers:
        if num == 0:
            arrangedList.append(num)
        else:
            arrangedList.insert(0,num)
    return arrangedList

print(arranged([5,0,34,9,0,13,8]))