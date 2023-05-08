
## Q1:Build a phone book program that receives the phone number 
# (Use Input to let the user provide the number), and returns the name of the owner. 



phone_guide={'Amal':'0568323222','Mohammed':'0522222232','Khadijah':'0532335983','Abdullah':'0545341144'
             ,'Rawan':'0545534556','Faisal':'0560664566','Layla':'0567917077'}

phone_belong_to = None


def number_exists (num):
    '''This Function checks if the number exists, then it will print the owner's name '''
    for k, v in phone_guide.items():
        if num == v:
            print("this phone number", v ,"is belongs to:", k)
            phone_belong_to = k
        return k


def number_length (num):
    '''this function checks the format of the input number if it is less
      or more than 10 numbers '''
    for v in phone_guide.items():
        if len(num) !=10:
            print("This is invalid number")
            break

def number_format(num):
    ''' This function checks if the number contains letters or symbols or not '''
    for v in phone_guide.items():
        if num.isnumeric()== False:
            print("This is invalid number, the number conatin letters or symbols")
            break


num = input("Please enter the phone number:")
number_exists(num)
number_length(num)
number_format(num)


## Q2:Write a function that receives a list containing the following numbers : 
# - [5, 0, 34, 9, 0, 13, 8]
# - rearranges the list so that the zeros are the end of the list, and finally returns the arranged list.

number_lisr=[5, 0, 34, 9, 0, 13, 8]

def rearranges_zeros_num (num):
    count = 0
    for i in range(len(num)):
        if num[i] != 0:
            num[i], num[count] = num[count], num[i]
            count += 1
    return num

print("the new arrange for the list is:",rearranges_zeros_num(number_lisr))
