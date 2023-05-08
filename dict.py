'''
If the number exists, print the owner. Otherwise, print "Sorry, the number is not found".
If the number is less or more than 10 numbers, print "This is invalid number".
If the number contains letters or symbols, print "This is invalid number".
'''

phone_book = {
    "0568323222": "Amal",
    "0522222232": "Mohammed",
    "0532335983": "Khadijah",
    "0545341144": "Abdullah",
    "0545534556": "Rawan",
    "0560664566": "Faisal",
    "0567917077": "Layla",
}


def find_owner(phone_number):
    if not phone_number.isdigit() or len(phone_number) != 10:
        return "This is invalid number."

    return phone_book.get(phone_number, "Sorry, the number is not found.")


phone_number = input("Enter a phone number: ")
result = find_owner(phone_number)
print(result)


'''
Q2:Write a function that receives a list containing the following numbers :
[5, 0, 34, 9, 0, 13, 8]
rearranges the list so that the zeros are the end of the list, and finally returns the arranged list.
'''


def rearrange_zeros(numbers):
    non_zeros = [num for num in numbers if num != 0]
    zeros = [0] * (len(numbers) - len(non_zeros))
    return non_zeros + zeros

numbers_list = [5, 0, 34, 9, 0, 13, 8]
arranged_list = rearrange_zeros(numbers_list)
print(arranged_list)
