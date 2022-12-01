str=" she is beautiful and she is good danccer"
print(str.replace(" ","_"))
print(str.replace("is","was"))

print(str.replace("is","was",1))

print(str.find("is"))#find to calculate position
print(str.find("is",6))

is_pos1=str.find("is")#number
is_pos2=str.find("is",is_pos1+1)
print(is_pos2)