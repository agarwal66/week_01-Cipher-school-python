name,char=input("enter comma separated name and character :").split(",")
print(f"length of your name is {len(name)}")
print(f"character count :{name.count(char)}")

# name.lower()
# char.lower()
print(f"character count :{name.lower().count(char.lower())}")
print(name.strip().lower().count(char.strip().lower()))