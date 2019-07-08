oak=list(input())
ink=[]
for j in oak:
   if j not in ink:
      ink.append(j)
if oak==ink:
   print("Yes")
else:
   print("No")


