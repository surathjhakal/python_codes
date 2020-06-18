def insertion_sort(lis):
    for i in range(1,len(lis)):
        value=lis[i]
        pos=i
        while pos>0 and lis[pos-1]>value:
            lis[pos]=lis[pos-1]
            pos-=1
        lis[pos]=value
    print(lis)
lis=[3,54,23,18,9,41,1]
insertion_sort(lis)
