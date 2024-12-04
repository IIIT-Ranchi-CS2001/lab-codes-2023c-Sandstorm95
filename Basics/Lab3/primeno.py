n = int(input("ente the no to be chek "))
h = n//2
while(h>1):
  if(n%h == 0):
    print("NO")
    break
  else:
    h = h-1
else: print("Yes")    