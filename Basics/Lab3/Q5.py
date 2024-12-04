n = input("Enter the object : ")
flag = True
for char in n:
  if not char.isalnum():
    flag = False
    break
print(flag)
