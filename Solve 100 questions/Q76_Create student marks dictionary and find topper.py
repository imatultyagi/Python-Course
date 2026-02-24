# Problem 76

n = int(input("Enter number of students: "))
students = {}

for _ in range(n):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks

topper = max(students, key=students.get)

print("Topper:", topper)
print("Marks:", students[topper])

# Sample Output:
# Enter number of students: 2
# Enter student name: Rahul
# Enter marks: 85
# Enter student name: Aman
# Enter marks: 92
# Topper: Aman
# Marks: 92