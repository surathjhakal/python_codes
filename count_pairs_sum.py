def pair_sum(arr,k):
    counter = 0
    lookup = set()
    for num in arr:
        if k-num in lookup:
            counter+=1
        else:
            lookup.add(num)
    print(counter)
    pass
pair_sum([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10)
