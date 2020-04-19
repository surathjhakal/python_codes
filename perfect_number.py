  
def perfect_number(n):
    total=0

    for i in range(1,n):
        if n%i==0:
            total=total+i
    return total

def main():

    n=int(input("enter a number"))
    sum=perfect_number(n)
    if sum==n:
        print(n,"it is a perfect number")
    else:
        print(n,"it is not a perfect number")
main()
