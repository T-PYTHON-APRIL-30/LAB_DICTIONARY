'''
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
If the number contains letters or symbols, print "This is invalid number".

Q2:Write a function that receives a list containing the following numbers :
[5, 0, 34, 9, 0, 13, 8]
rearranges the list so that the zeros are the end of the list, and finally returns the arranged list.
'''
#Q1
numbers_dictionary = {
    "0568323222":"Amal",
    "0522222232":"Mohammed",
    "0532335983": "Khadijah",
    "0545341144": "Abdullah",
    "0545534556":"Rawan",
    "0560664566":"Faisal",
    "0567917077" :"Layla"
}

user_input = input("Provide the number: ")

if user_input.isdigit() and len(user_input) ==10:
    print(f'The name of the owner: {numbers_dictionary.get(user_input," Sorry, the number is not found")}')   
else:
    print("This is invalid number")


#Q2 
int_list=[5, 0, 34, 9, 0, 13, 8]
print(f"Before arrange the list: {int_list}")
def rearranges_list(list1 : list)->list:
    arranged_list=list1[:]
    arranged_list.sort(reverse=True)
    return arranged_list

print(f"After arrange the list: {rearranges_list(int_list)}")
#print(int_list)