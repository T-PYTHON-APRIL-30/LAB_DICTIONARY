#Q1
phone_book = {
    "0568323222": "Amal",
    "0522222232": "Mohammed",
    "0532335983": "Khadijah",
    "0545341144": "Abdullah",
    "0545534556": "Rawan",
    "0560664566": "Faisal",
    "0567917077": "Layla"
}

input_user = input("Enter the number\n > ")
if len(input_user) != 10 or input_user.isdigit() == False:
    print("This is invalid number")
elif input_user in phone_book:
    print(f"The owner is '{phone_book[input_user]}'")
else:
    print("Sorry, the number is not found")


#Q2
numbers = [5, 0, 34, 9, 0, 13, 8]

def list_number(number: list) -> list:
    for num in number:
        if num == 0:
            number.remove(num)
            number.append(num)
    return number


print(list_number(numbers))