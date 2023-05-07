
number_book={"0568323222":"Amal","0522222232":"Mohammed","0532335983":"Khadijah",
             "0545341144":"Abdullah","0545534556":"Rawan","0560664566":"Faisal"
             ,"0567917077":"Layla"}
# Q1 ---------------------------------
def number_check(key_number,book):
    if len(key_number)>10 or len(key_number)<10 or not key_number.isdigit():
        print("This is invalid number")
    elif key_number in book:
        print(f"the owner is {book[key_number]}")
    else:
        print("Sorry, the number is not found")

number_check("0545341144",number_book)

# Q2 ---------------------------------
new_list=[5, 0, 34, 9, 0, 13, 8]

def rearranges_zeros(list1:list):
    len_of_list=len(list1)
    for n in range(0,len_of_list):    
       
        if list1[n]==0: 
            change=list1[n]
            list1.append(change)
            list1.pop(n)
           
    return list1

print(rearranges_zeros(new_list))




