fake=int(input())
if (fake<=1000):
   for i in range(2,fake):
       if(fake%i==0):
         print("no")
         break
   else:
       print("yes")
else:
    print("no")
         
