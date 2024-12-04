n = int(input("Enter n "))
i = 0
sum = 0
prev1 = 1
prev2 = 0
if(i == 0):
  print(0)
while(i <= n):
  sum = prev1 + prev2
  print(sum)
  prev1 = prev2
  prev2 = sum
  prev = sum
  i = i+1
