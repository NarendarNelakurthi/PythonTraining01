import sys
students = ["akram", "trusha", "bhavana", "jaya", "chaitra"]

print("Break statement")
for student in students:
    if student=="bhavana":
        break
    else:
        print(f' The student name is {student}')
print("Pass statement")
for student in students:
    if student=="trusha":
        pass
    else:
        print(f' The student name is {student}')
print("Continue statement")
for student in students:
    if student=="trusha":
        continue
    else:
        print(f' The student name is {student}')
print("sys statement")
for student in students:
    if student=="trusha":
        sys.exit(0)
    else:
        print(f' The student name is {student}')