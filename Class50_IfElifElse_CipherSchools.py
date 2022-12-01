age=int(input("enter age"))
if age==0:
    print("you can't watch")
elif 0<age<=3:
    print("ticket is free")
elif 3<age<=10:
    print("ticket price is 150")
elif 10<age<=60:
    print("ticket price is 250")
else:    
    print("ticket price is 200")          