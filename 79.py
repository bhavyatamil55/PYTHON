vish,desk=map(int,input().split())
vish=vish*desk
for i in range(0,vish+1):
 if(i**2==0):
  print("yes")
  break
else:
 print("no")
