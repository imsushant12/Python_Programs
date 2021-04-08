n = int(input("Enter number of students : "))
print("Enter marks : ")
i=0
students = []
for i in range(n):
    a = int(input())
    students.insert(i,a)

students.sort()
print(students)

