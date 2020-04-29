import random
def random_password(n,digit,lower,upper,sym):
    password=''
    if n=='' and n<8:
        n=8
    else:
        for i in range(1,n+1):
            num=random.randint(1,4)
            if num==1:
                r=random.choice(digit)
            elif num==2:
                r=random.choice(lower)
            elif num==3:
                r=random.choice(upper)
            else:
                r=random.choice(sym)
            password+=r
        print(f"your password is {password}")
def main():
    digit= ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']   
    lower=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',  
                         'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 
                         'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 
                         'z'] 

    upper= ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',  
                         'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q', 
                         'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 
                         'Z'] 

    sym= ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',  
               '*', '(', ')', '<&# 039']
    n=int(input("how much length of password you want but 8 length of is default"))
    random_password(n,digit,lower,upper,sym)
main()
