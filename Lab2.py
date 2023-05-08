# LAB_DICTIONARY


# Q1:Build a phone book program that receives the phone number
# (Use Input to let the user provide the number), and returns the name of the owner.

phone_book = {

    "0568323222": "Amal",
    "0522222232": "Mohammed",
    "0532335983": "Khadijah",
    "0545341144": "Abdullah",
    "0545534556": "Rawan",
    "0560664566": "Faisal",
    "0567917077": "Layla"
}
phone_number = input("Please enter a phone number: ")
if phone_number in phone_book:
    print(phone_book[phone_number])
elif len(phone_number) != 10:
    print("This is invalid number")
elif phone_number.isdigit() != True:
    print("This is invalid number")
else:
    print("Sorry, the number is not found")

# Q2:Write a function that receives a list containing the following numbers :
'''- [5, 0, 34, 9, 0, 13, 8]
- rearranges the list so that the zeros are the end of the list, and finally returns the arranged list.'''
my_list = [5, 0, 34, 9, 0, 13, 8]
i = 0
# print(my_list[0],"ll",my_list.index(0),"ll")
for i in range(0, len(my_list)):

    if my_list[i] == 0:
        zeros = my_list.pop(i)
        my_list.append(zeros)
print(my_list)
