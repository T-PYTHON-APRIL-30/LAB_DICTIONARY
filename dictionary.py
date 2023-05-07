phone_dictionary = {"Amal" : "0568323222",
                    "Mohammed" : "0522222232", 
                    "Khadijah" : "0532335983",
                    "Abdullah" : "0545341144",
                    "Rawan" : "0545534556",
                    "Faisal" : "0560664566",
                    "Layla" : "0567917077"}

print (phone_dictionary)

#1__________________________________________________________________________________
def phone_exsist(phone_dictionary, user_input):
    keys = [ke for ke, check in phone_dictionary.items() if check == user_input]
    if keys:
        return print("owner is: ",keys[0])
    elif user_input > str(10) or user_input <str(10) or user_input.isalpha() or user_input.isalnum():
        print("This is invalid number")

    else: 
        print("Sorry, the number is not found")
    
    
key = phone_exsist(phone_dictionary,str(input()))
print(key)

#2__________________________________________________________________________________
lst = [5, 0, 34, 9, 0, 13, 8]
new_lst = lst
new_lst.sort(reverse=True)
print(new_lst)


