def happy_number(n):
    s=n
    c=0
    while c<=50:
        if s==1:
            print("it is a happy number")
            break
        else:
            total=0
            for i in str(s):
                total+=(int(i)**2)
            s=total
            if c==50:
                print("it is not a happy number")
                break
            c+=1
            continue
def main():
    n=int(input("enter the number"))
    happy_number(n)
main()
