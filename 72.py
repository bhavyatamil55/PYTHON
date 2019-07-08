inputs=input()
ijk=['a','e','i','o','u']
zen=any(c in inputs for c in ijk)
if(zen==True):
  print('yes')
else:
  print('no')
