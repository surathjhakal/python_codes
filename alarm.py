import datetime
def alarm(hour,mint,sec,repeat):
    for i in range(1,repeat+1):    
        while True:
            if (hour==datetime.datetime.now().hour and
               mint==datetime.datetime.now().minute and
               sec==datetime.datetime.now().second):
                print("wake up man")
                print("BUZZ")
                mint+=1
                break


    print("alarm ended")
def main():
    hour=int(input("enter the hour you want to wake up"))
    mint=int(input("enter the min you want to wake up"))
    sec=int(input("enter the sec you want to wake up"))
    repeat=int(input("enter after how many minute you want to repeat this alarm"))
    alarm(hour,mint,sec,repeat)
main()
