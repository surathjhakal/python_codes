def anagrams(n1,n2):
    n1=n1.lower()
    n1=n1.strip()
    n2=n2.lower()
    n2=n2.strip()
    c=0
    for i in n1:
        if i not in n2:
            c+=1
            break
    print(n1)
    print(n2)
    if c<1:
        print("it is a anagram string")
    else:
        print("it is not a anagram string")
def main():

    n1=input("enter a word ")
    n2=input("enter another word")
    anag=anagrams(n1,n2)
    print(anag)
main()
