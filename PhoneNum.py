'''LAB_DICTIONARY
Q1:Build a phone book program that receives the phone number (Use Input to let the user provide the number), and returns the name of the owner.
You can follow the table below:

Name	Number
Amal	0568323222
Mohammed	0522222232
Khadijah	0532335983
Abdullah	0545341144
Rawan	0545534556
Faisal	0560664566
Layla	0567917077
If the number exists, print the owner. Otherwise, print "Sorry, the number is not found".
If the number is less or more than 10 numbers, print "This is invalid number".
If the number contains letters or symbols, print "This is invalid number".'''
phoineNum={568323222:"Amal",522222232:"Mohammed",532335983:"Khadijah",
           545341144:"Abdullah",545534556:"Rawan",560664566:"Faisal",
           567917077:"Layla"
           }
print("please give me a phone number without starting with zero:")
Number=input()
#If the number exists, print the owner. Otherwise, print "Sorry, the number is not found".
if Number.isdigit()==True and len(Number)==9 and Number!=" ":
    Name=phoineNum[Number]
    print(f"the owner of the number{Number}is{Name}")
elif Number==" ":
    print("Sorry, the number is not found")
    print("please give me a phone number without starting with zero:")
elif len(Number)<9 or len(Number)>9:
    print("This is invalid number")
    print("please give me a phone number without starting with zero:")
elif Number.isdigit()==False:
    print("This is invalid number")
    print("please give me a phone numberwithout starting with zero:")
'''Q2:Write a function that receives a list containing the following numbers :
[5, 0, 34, 9, 0, 13, 8]
rearranges the list so that the zeros are the end of the list, and finally returns the arranged list'''
def RearrangeList():
    rearrangList=[5, 0, 34, 9, 0, 13, 8]
    ZerosList=[0,0]
    rearrangList.extend(ZerosList)
    popedItem=rearrangList.pop(0)
    NewList=rearrangList+ZerosList
    return NewList
RearrangeList()




