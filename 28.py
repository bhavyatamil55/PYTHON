bhav=int(input())
sak=list(map(int,input().split()[:bhav]))
for s in range(bhav):
  print(sak[s],s)
