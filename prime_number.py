
def prime(n):
    list1=[2]
    c=0
    if n<3:
        return list1
    for i in range(3,n+1):
        for j in list1:
            if i%j==0:
                break
        else:
            list1.append(i)
                
                    
    return list1
n=int(input("enter a integers"))
prime(n)
