    
n1=int(input())
temp=n1
rev1=0
while(n1>0):
    d=n1%10
    rev1=rev1*10+d
    n1=n1//10
if(temp==rev1):
    print("yes")
else:
    print("no")
