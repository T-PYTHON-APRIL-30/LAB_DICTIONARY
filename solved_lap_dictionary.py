my_dictionary = { '0568323222' : "Amal", '0522222232' : "Mohammed", '0532335983' : "Khadijah",
                 '0545341144' : "Abdullah", '0545534556' : "Rawan", '0560664566' : "Faisal", '0567917077' : "Layla"}

def check_owner(number:str):
    result = 0
    check_count = number

    for n in my_dictionary:
        if number == n:
            result = 1
            name = n
            break
        
    if result == 1:
        print("The owner is:",my_dictionary[name])
        
    elif result == 0:
        print("sorry the number is not found")

    if len(number) > 10 or len(number) < 10:
        print("this is more or less than 10 digits")

    
    if number.isnumeric != True:
        print("this is invalid number")

check_owner(input("Enter a number to find the owner:"))

#Qustion 2
list_numbers = [5, 0, 34, 9, 0, 13, 8]
def arreanged(new_list:list) -> list:
    arreanged_list = []
    for a in new_list:
        if a == 0:
            arreanged_list.append(0)

        elif a != 0:
            arreanged_list.insert(0,a)

    return arreanged_list



print(arreanged(list_numbers))