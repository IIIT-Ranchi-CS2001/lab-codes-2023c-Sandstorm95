
names = [f"Student{i}" for i in range(1, 11)]
roll_nos = [i for i in range(1, 11)]
marks = [80 + i for i in range(10)]


students = []
for i in range(len(names)):
    students.append((names[i], roll_nos[i], marks[i]))

3
n = len(students)
for i in range(n):
    for j in range(0, n-i-1):
        if students[j][2] > students[j+1][2]:
            students[j], students[j+1] = students[j+1], students[j]


for student in students:
    print(student)
