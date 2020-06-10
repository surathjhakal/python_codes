#ouptut:A1a3b2c4d1
def compress(s):
    d={}
    count=1
    for i in range(len(s)):
        if s[i] not in d:
            count=1
            d[s[i]]=count
        else:
            count+=1
            d[s[i]]=count
    for i,j in d.items():
       print('{}{}'.format(i,j),end='')
s='Aaaabbccccd'
a=compress(s)
