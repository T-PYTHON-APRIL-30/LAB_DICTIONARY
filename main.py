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

phone_number = input("Enter the phone number: ")

if len(phone_number) != 10 or not phone_number.isdigit():
    print("This is an invalid number.")
else:
    owner = phone_book.get(phone_number)
    if owner:
        print("Owner:", owner)
    else:
        print("Sorry, the number is not found.")


#Q2

def rearrange_zeros(lst):
    zeros = lst.count(0)  
    while 0 in lst:
        lst.remove(0)  
    lst.extend([0] * zeros) 
    return lst

my_list = [5, 0, 34, 9, 0, 13, 8]
arranged_list = rearrange_zeros(my_list)
print(arranged_list)
