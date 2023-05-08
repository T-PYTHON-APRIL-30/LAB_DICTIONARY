"""# LAB_DICTIONARY


## Q1:Build a phone book program that receives the phone number (Use Input to let the user provide the number), and returns the name of the owner. 
You can follow the table below:

| Name    | Number      |
| -------- | ---------- |
| Amal     | 0568323222 |
| Mohammed | 0522222232 |
| Khadijah | 0532335983 |
| Abdullah  | 0545341144 |
| Rawan    | 0545534556 |
| Faisal   | 0560664566 |
| Layla    | 0567917077 |


- If the number exists, print the owner. Otherwise, print "Sorry, the number is not found".
- If the number is less or more than 10 numbers, print "This is invalid number".
- If the number contains letters or symbols, print "This is invalid number".

## Q2:Write a function that receives a list containing the following numbers : 
- [5, 0, 34, 9, 0, 13, 8]
- rearranges the list so that the zeros are the end of the list, and finally returns the arranged list.
"""
phoneBook = {
    "Amal": "0568323222",
    "Mohammed": "0522222232",
    "Khadijah": "0532335983",
    "Abdullah": "0545341144",
    "Rawan": "0545534556",
    "Faisal": "0560664566",
    "Layla": "0567917077"
}


number = input("Enter a phone number: ")

if not number.isdigit() or len(number) != 10:
    print("This is an invalid number")
else:
    owner = False
    for name, num in phoneBook.items():
        if num == number:
            owner = name
            break
    if owner != False:
        print(owner)
    else:
        print("Sorry, the number is not found")


# Function to rearrange list with zeros at the end

def rearrange_zeros(lst):
    zeros = lst.count(0)
    new_lst = [num for num in lst if num != 0]
    new_lst.extend([0] * zeros)
    
    return new_lst


# Example usage
lst = [5, 0, 34, 9, 0, 13, 8]
new_lst = rearrange_zeros(lst)
print(new_lst) # Output: [5, 34, 9, 13, 8, 0, 0]