tag=int(input())
em1,em2=0,1
print(em2,end=" ")
for i in range(1,tag):
 em3=em1+em2
 print(em3,end=" ")
 em1,em2=em2,em3
