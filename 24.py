vsb=int(input())
ssb=list(map(int,input().split()[:vsb]))
ssb.sort()
for skp in ssb:
	print(skp,end=" ")
