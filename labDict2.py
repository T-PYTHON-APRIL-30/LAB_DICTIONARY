myList=[5, 0, 34, 9, 0, 13, 8]
def rearranges_list(myList : list):
    ZeroList=myList[:]
    ZeroList.sort()
    ZeroList.reverse()
    return ZeroList

print(f"After modifying the list: {rearranges_list(myList)}")