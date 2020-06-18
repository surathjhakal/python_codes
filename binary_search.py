def binary_search(list1,ele):
    found=False
    f=0
    l=len(list1)-1
    pos=0
    while pos<len(list1) and not found:
        mid=(f+l)//2
        if list1[mid]==ele:
            found=True
        elif list1[mid]>ele:
            l=mid-1
        else:
            f=mid+1
        pos+=1
    return found

list1=[2,23,45,65,87,91,98]
ele=91
s=binary_search(list1,ele)
if s:
    print("number found")
else:
    print("number not found")
