def armstrong(n):
    total=0
    temp=n
    while n>0:
        r=n%10
        total+=r**3
        n=n//10
    if temp==total:
        print("the number",temp,"is a armstrong number")
    else:
        print("the is not a armstrong number")
def main():

    n=int(input("enter a number"))
    arm=armstrong(n)
    print(arm)
main()
