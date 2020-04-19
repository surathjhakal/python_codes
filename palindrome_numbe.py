
def palindrome(n):
    sum=0
    temp=n
    while n>0:
        r=n%10
        sum=sum*10+r
        n=n//10
    if temp==sum:
        return "true"
    else:
        return "false"
def main():


    n=int(input("enter a number"))
    palin=palindrome(n)
    print(palin)
main()
