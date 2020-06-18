def bubble_sort(l):
    for i in range(len(l),0,-1):
        for j in range(i-1):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
    print(l)
l=[75,3,2,8,31,1]
bubble_sort(l)
