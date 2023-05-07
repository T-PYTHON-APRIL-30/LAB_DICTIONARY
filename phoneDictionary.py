'''Q1:Build a phone book program that receives the phone number (Use Input to let the user provide the number),
 and returns the name of the owner.
You can follow the table below:

Name	Number
Amal	0568323222
Mohammed	0522222232
Khadijah	0532335983
Abdullah	0545341144
Rawan	0545534556
Faisal	0560664566
Layla	0567917077

*If the number exists, print the owner. Otherwise, print "Sorry, the number is not found".
*If the number is less or more than 10 numbers, print "This is invalid number".
*If the number contains letters or symbols, print "This is invalid number".'''

def searchPhoneNum (num:str, myDict:dict) -> str:

    for key, value in myDict.items():
        if value == num:
            return f'The owner of this number is {key}'
        
    else:
        return 'Sorry, the number is not found!'

            

phoneBook = {'Amal':'0568323222', 'Mohammed': '0522222232', 'Khadijah': '0532335983',
              'Abdullah':'0545341144', 'Rawan':'0545534556', 'Faisal':'0560664566','Layla':'0567917077'}

phoneNumber = input('Please enter the phone number: ')

if phoneNumber.isdigit() == True and len(phoneNumber) == 10:
    print(searchPhoneNum(phoneNumber,phoneBook))

else:
    print('Invalid phone Number!!')