#Q1
phone_book = {
    "Amal": "0568323222",
    "Mohammed": "0522222232",
    "Khadijah": "0532335983",
    "Abdullah": "0545341144",
    "Rawan": "0545534556",
    "Faisal": "0560664566",
    "Layla": "0567917077"
}

input_user = input("Enter the number\n > ")
if len(input_user) != 10 or input_user.isdigit() == False:
    print("This is invalid number")


for key, value in phone_book.items():
    if input_user == value:
        print(f"The owner is '{key}'")
    else:
        print("Sorry, the number is not found")


#Q2
numbers = [5, 0, 34, 9, 0, 13, 8]

def list_number(number: list) -> list:
    for num in number:
        if num == 0:
            number.remove(num)
            number.insert(-1, num)
    return number


print(list_number(numbers))