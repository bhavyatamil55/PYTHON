flag=0
a,b=input().split()
a=int(a)
b=int(b)
arm=[int(i) for i in input().split()]
z=b
if z in arm:
  print('yes')
else:
  print('no')
