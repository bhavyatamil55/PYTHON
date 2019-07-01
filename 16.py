b,s=map(int,input().split())
for p in range(b+1,s,1):
    if(p>1):
        for m in range(2,p):
            if(p%m==0):
                break
        else:
            print(p,end=" ")
