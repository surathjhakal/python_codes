cal = True


class calculator:
    def formation():
        print("Enjoy using my calculator")
        print()
        print("!!!!CALCULATOR!!!!!!")
        print()
        print("| --- || --- || --- |_____")
        print("|  1  ||  2  ||  3  |___+_|")
        print("| --- || --- || --- |_____")
        print("| --- || --- || --- |___-_|")
        print("|  4  ||  5  ||  6  |_____")
        print("| --- || --- || --- |___*_|")
        print("| --- || --- || --- |_____")
        print("|  7  ||  8  ||  9  |___\_|")
        print("| --- || --- || --- |")

    def user_input():
        global n
        global ans
        global c
        c = 0
        n = input("what ever calculation u want to do just write it over here:\n")
        try:
            ans = eval(n)
            c += 1
            return ans
        except:
            print("Please put correct values and signs")


while cal:
    calculation1 = calculator
    calculator.formation()
    calculator.user_input()
    if c == 1:
        print(f"The answer of your {n}: {ans}")
    again = input("If you want to do calculation again then enter y for yes or n for no\n")
    if again.lower() == 'y':
        continue
    else:
        cal = False
        print()
        print("Thank you for using my calculator")
        print()
        break
