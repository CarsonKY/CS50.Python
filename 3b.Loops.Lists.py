# List of students

# print student #2

students = ["Jeff", "James", "Mary"]

# Printing student #2 (index 1 in Python, since indexing starts at 0)
print("Student #2:", students[1])

# print all students
students = ["Jeff", "James", "Mary"]

for student in students:
    print (student)

# print full list with description

students = ["Jeff", "James", "Mary"]

# Printing all students in the specified format
for i, student in enumerate(students, start=1):
    print(f"Student number {i} is {student}")

# Using Len to get length of list

students = ["Jeff", "James", "Mary"]

for i in range(len(students)):
    print (i + 1, students[i])
