a = int(input("Enter marks of subject 1 "))
b = int(input("Enter marks of subject 2 "))
c = int(input("Enter marks of subject 3 "))

#33 percent is required for each subject. So,
#least_subject_marks = 33

if (a > 33) and (b > 33) and (c > 33):
    pass
else:
    print("Failed in one subject")

total = a+b+c

#40 % of 300 is 120

if total > 120:
    print("Pass in all subjects, Percentage = ", total/300, "%")
else:
    print("Failed overall")