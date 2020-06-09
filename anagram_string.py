def anagram(o,n):
    o=o.replace(' ','')
    n=n.replace(' ','')
    for i in o:
        if i not in n and len(n)<=0:
            return False
        else:
            n=n.replace(i,'',1)
    if len(n)==0:
        return True

o="old west action"
n="clint eastwood"
a=anagram(o,n)
if a==True:
    print("It is an anagram")
else:
    print("it is not an anagram")

