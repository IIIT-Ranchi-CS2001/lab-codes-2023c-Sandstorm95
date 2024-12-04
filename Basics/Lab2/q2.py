s = "Ba Ba Black Sheep"
print(len(s))
for i in s:
    if i == 'e':
        print(s.index(i))
        break;

countA = 0
for i in s:
    if i == 'a':
        countA += 1
print(countA)

s1 = s[0:5]
s2 = s[5:17]
s3 = s1.replace('B', 'T')+s2
print(s3)