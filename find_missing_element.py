import random
def find(o,n):
    print(o)
    print(n)
    for i in o:
        if i not in n:
            number=i
            break
    print("the missing number is {}".format(number))

o=[1,2,3,4,5,6,7]
n=o.copy()
random.shuffle(n)
n.pop()
find(o,n)
