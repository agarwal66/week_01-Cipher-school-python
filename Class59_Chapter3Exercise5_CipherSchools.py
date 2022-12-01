a=input("enter your name")
temp=""

i=0
while i<len(a):
    if a[i] not in temp:
        temp+=a[i]
        print(f"{a[i]}:{a.count(a[i])}")
    i+=1