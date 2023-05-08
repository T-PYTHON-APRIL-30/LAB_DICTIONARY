#1-Build a phone book program that receives the phone numbe
#(Use Input to let the user provide the number), and returns the name of the owner.

phone_book = {
    "Amal":"0568323222",
    "Mohammed":"052222222232",
    "Khadijah":"0532335083",
    "Abduallah":"0545341144",
    "Rawan": "05455345556",
    "Faisal": "0560664566",
    "Laila": "0567917077",
}
number = input("Enter Phone Number:")
for name, num in phone_book.items():
    if num == number:
        print "Name Of Owner", name)
    if num <= 10
       print "his is invalid number"
     break
      else:
      print("Sorry, the number is not found")
    

    #Write a function that receives a list containing the following numbers :
#[5, 0, 34, 9, 0, 13, 8]
#rearranges the list so that the zeros are the end of the list, and finally returns the arranged list

def rearrange_zeros(lst):
zeros = []
non_zeros = []
for num in lst:
   if num == 0"
      zeros.append(num)
   else:
      non_zeros + zeros
lst = [5, 0, 34, 9, 0, 13, 8]
print (rearrange_zeros(lst))



