#output:'best the is this'
def sentence(s):
    word=''
    s+='.'
    sentence=''
    for i in range(len(s)):
        if s[i]==' ' or s[i]=='.':
            sentence=word+' '+sentence
            word=''
        else:
            word+=s[i]
    return sentence

s='this is the best'
a=sentence(s)
print("the new reverse sentence is : {}".format(a))
