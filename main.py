# --------------- LAB_DICTIONARY ---------------
print("------- Q1 -------")
numberDic = { 
    '0568323222' : "Amal", 
    '0522222232' : "Mohammed", 
    '0532335983' : "Khadijah",
    '0545341144' : "Abdullah",
    '0545534556' : "Rawan",
    '0560664566' : "Faisal", 
    '0567917077' : "Layla"
    }

def checkLen(number):
    '''This fun check if the number is it 10 numbers or not ! '''
    if len(number) != 10 :
       print("Wrong number !!")
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
        print("The number is not exist !!")

checkLen(input("Enter the phone number: "))