#generate random numbers
wn=10
a=int(input("enter number"))
if a==wn:
    print("you win")
else:
    if a<wn:
        print("too low")
    if a>wn:
        print("too high")
    