import math as m
a = int(input("Enter the a: "))
b = int(input("Enter the b: "))
c = int(input("Enter the c: "))
s = (a+b+c)/2
d = m.sqrt(s*(s-a)*(s-b)*(s-c))
print("The area of the triangle is ",d)
AngleA = m.acos((b*b + c*c - a*a)/2*b*c)
print("AngleA in radians:", AngleA)

