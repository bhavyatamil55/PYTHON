b,s=map(int,input().split())
for num in range(b+1,s):
   sum = 0
   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** 3
       temp //= 10
   if num == sum:
       print(num,s=' ')
