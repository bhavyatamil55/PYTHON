fun=int(input())
zan=list(map(int,input().split()))
for i in range(len(zan)-1):
   if(zan[i]>zan[i+1]):
      print(i)
