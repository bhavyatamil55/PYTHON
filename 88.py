bhav1,bhav2=map(int,input().split())
maximum=max(bhav1,bhav2)
while(1):
   if(maximum%bhav1==0 and maximum%bhav2==0):
          print(maximum)
          break
   maximum+=1
