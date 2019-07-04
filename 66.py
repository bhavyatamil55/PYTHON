srii=int(input())
temp=srii
if(srii==2):
  print('yes')
elif(srii % 1 ==0 and srii % temp==0 and srii%2!=0 and srii%3!=0 and srii%4!=0):
  print('yes')
else:
  print('no')
