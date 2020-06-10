def unique(s):
    new=''
    c=0
    for i in s:
        if i in new:
            c+=1
            break
        else:
            new+=i
    if c<1:
        print("all character are unique in string")
    else:
        print("all character are not unique in string")
s='abcde'
unique(s)
