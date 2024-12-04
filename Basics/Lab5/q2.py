# lists
names = [f"Student{i}" for i in range(1, 11)]
roll_nos = [i for i in range(1, 11)]
marks = [80 + i for i in range(10)]

# Create a list of tuples using zip
students = list(zip(names, roll_nos, marks))

# Sort the list of tuples by marks
sorted_students = sorted(students, key=lambda x: x[2])

# Print the sorted list
for student in sorted_students:
    print(student)
