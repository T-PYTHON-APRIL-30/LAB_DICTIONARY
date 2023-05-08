phone_number = input("Please enter the phone number: ")
def get_owner(phone_number):
    phone_book = {"0568323222": "Amal","0522222232": "Mohammed","0532335983": "Khadijah","0545341144": "Abdullah","0545534556": "Rawan","0560664566": "Faisal","0567917077": "Layla"}
    if not phone_number.isdigit() or len(phone_number) != 10:
       return "This is an invalid number"
    owner = phone_book.get(phone_number)
    if owner is not None:
      return owner
    else:
     return "Sorry, the number is not found"
result = get_owner(phone_number)
print(result)