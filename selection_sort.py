def selection_sort(list2):
    for i in range(len(list2)-1):
        min=i
        for j in range(i+1,len(list2)):
            if list2[min]>list2[j]:
                min=j
        list2[i],list2[min]=list2[min],list2[i]
    print(list2)
list2 = [75,3,2,8,31,1,2]
selection_sort(list2)
