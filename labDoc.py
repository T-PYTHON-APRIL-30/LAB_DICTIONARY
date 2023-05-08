phone_book = {

    "0568323222": "Amal",
    "0522222232": "Mohammed",
    "0532335983": "Khadijah",
    "0545341144": "Abdullah",
    "0545534556": "Rawan",
    "0560664566": "Faisal",
    "0567917077": "Layla"
}

#num = input("Enter a number: ")
flag = True
while flag:
     num = input("Enter a number: ")
     if num in phone_book:
          print(phone_book[num])
          flag = False
     elif len(num) != 10:
          print("this is invalid number")
     elif num.isdigit() != True:
          print("this is invalid")


#------------

listN = [5,0,34,9,0,13,8]

def arrangeList(givenList : list):
     lengthList = len(givenList)

     for number in range(0,lengthList):
          if givenList[number] == 0:
               changedZero = givenList[number]
               givenList.append(changedZero)
               givenList.pop(number)

     return givenList

print(arrangeList(listN))