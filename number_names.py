#9923: nine thousand nine hundred twenty three
#523: five hundred twenty three
#89: eighty nine
def number_names(n):
    word=''
    numbers={1:'One',2:'Two',3:'Three',4:'four',5:'five',6:'six',7:'seven',8:'eigth',9:'nine',10:'ten',
            11:'eleven',12:'Twelve',13:'Thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',
            18:'eighteen',19:'nineteen',20:'twenty',30:'thirty',40:'forty',50:'fifty',60:'sixty',70:'seventy',80:'eighty',
            90:'ninty'}
    word=''
    
    if int(n)<=20:
        word+=numbers[int(n)]
    else:
        n=n[::-1]
        for i in range(len(n)): #501
            if i==0 and n[i]!='0':
                word=numbers[int(n[i])]+' '+word
            elif i==1 and n[i]!='0':
                word=numbers[int(n[i]+'0')]+' '+word
            elif i==2 and n[i]!='0':
                word=numbers[int(n[i])]+' '+'hundred'+' '+word
            elif i==3:
                word=numbers[int(n[i])]+' '+'thousand'+' '+word
            else:
                continue
    print(word)

def main(): 
    n=input("enter the number ")
    number_names(n)
main()
