def shell_sort(lis):
    gap=len(lis)//2
    while gap>0:
        for i in range(gap,len(lis)):
            value=lis[i]
            pos=i
            while pos>0 and lis[pos-gap]>value:
                lis[pos]=lis[pos-gap]
                pos-=1
            lis[pos - gap]=value
        gap=gap//2
    print(lis)


lis=[3,54,23,18,9,41,1,2]
insertion_sort(lis)
