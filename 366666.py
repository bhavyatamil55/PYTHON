vsb=input()
sen=0
for i in range(len(vsb)):
 if(vsb[i].isdigit() or vsb[i].isalpha() or vsb[i]==(" ")):
  continue
 else:
  sen+=1
print(sen)
