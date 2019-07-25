leapyear=int(input())
if((leapyear%4==0) and (leapyear%100!=0)):
    print("yes")
elif(leapyear%100==0):
    print("no")
elif(leapyear%400==0):
    print("yes")
else:
    print("no")
