sam=input()
count=0
for i in range(len(sam)):
 if(sam[i].isdigit() or sam[i].isalpha() or sam[i]==(" ")):
  continue
 else:
  count+=1
print(count)
