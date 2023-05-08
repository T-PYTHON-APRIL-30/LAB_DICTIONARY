'''
# LAB_DICTIONARY


## Q1:Build a phone book program that receives the phone number (Use Input to let the user provide the number), and returns the name of the owner. 
You can follow the table below:

| Name     | Number     |
| -------- | ---------- |
| Amal     | 0568323222 |
| Mohammed | 0522222232 |
| Khadijah | 0532335983 |
| Abdullah | 0545341144 |
| Rawan    | 0545534556 |
| Faisal   | 0560664566 |
| Layla    | 0567917077 |


- If the number exists, print the owner. Otherwise, print "Sorry, the number is not found".
- If the number is less or more than 10 numbers, print "This is invalid number".
- If the number contains letters or symbols, print "This is invalid number".
'''
phoneBook = {
    "0568323222" : "Amal",
    "0522222232" : "Mohammed",
    "0532335983" : "Khadijah",
    "0545341144" : "Abdullah",
    "0545534556" : "Rawan",
    "0560664566" : "Faisal",
    "0567917077" : "Layla"
}
number = input("Enter the number you would search: ")
if len(number) != 10 and not number.isdigit:
    print("This is invalid number")
if phoneBook.get(number, -1) == -1:
    print("Sorry, the number is not found")
else:
    print(f"the name of the number ({number}) is {phoneBook[number]}")
'''

## Q2:Write a function that receives a list containing the following numbers : 
- [5, 0, 34, 9, 0, 13, 8]
- rearranges the list so that the zeros are the end of the list, and finally returns the arranged list.

'''
def zeroEnd(list : list):
    for index in range(len(list)):
        if list[index] == 0:
            list.pop(index)
            list.append(0)
    
list = [5, 0, 34, 9, 0, 13, 8]
zeroEnd(list)
print(list)