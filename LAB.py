'''
If the number exists, print the owner. Otherwise, print "Sorry, the number is not found".
If the number is less or more than 10 numbers, print "This is invalid number".
If the number contains letters or symbols, print "This is invalid number".
'''
BookNumber = {
    "0568323222": "Amal",
    "0522222232": "Mohammed",
    "0532335983": "Khadijah",
    "0545341144": "Abdullah",
    "0545534556": "Rawan",
    "0560664566": "Faisal",
    "0567917077": "Layla"
}
phone_number = input("Enter a phone number: ")
if phone_number in BookNumber:
    print(BookNumber[phone_number])
if len(phone_number) != 10:
    print("This is invalid number")
else:
    print("Sorry, the number is not found")
