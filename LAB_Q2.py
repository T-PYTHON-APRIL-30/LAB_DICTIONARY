'''
[5, 0, 34, 9, 0, 13, 8]
rearranges the list so that the zeros are the end of the list,
 and finally returns the arranged list.
'''
list=[5, 0, 34, 9, 0, 13, 8]
New_list=(list)
lenlist=len(New_list)
for element in range(0,lenlist):    
    if New_list[element]==0: 
        replace=New_list[element]
        New_list.append(replace)
        New_list.pop(element)
print(list)

