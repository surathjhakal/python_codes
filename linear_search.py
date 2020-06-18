def linear_serach(list1,ele):
    found=False
    i=0
    while i<len(list1) and not found:
        if list1[i]==ele:
            found=True
        i+=1
    return found
list1=[2,23,45,65,87,91,98]
ele=91
s=linear_serach(list1,ele)
if s:
    print("number found")
else:
    print("number not found")

