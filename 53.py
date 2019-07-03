    
Name=int(input())
s=0
i=0
while(Name>0):
    i=Name%10
    s=s+i
    Name=Name//10
print(s)
