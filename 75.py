vsb=list(input())
if len(vsb)%2==0:
    vsb[int(len(vsb)/2)] ='*'
    vsb[int(len(vsb)/2)-1]='*'
else:
    vsb[int(len(vsb)/2)] ='*'
for i in range(0,len(vsb)):
    print(vsb[i],end='')
