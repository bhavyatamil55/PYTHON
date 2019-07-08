srii=input()
array=[]
if(srii.isdigit()==True):
  for i in srii:
    if(int(i)%2!=0):
      array.append(i)
print(*array)
