#to calculate average height of students formula : - sum of height students / no of students

students_height = input("Input the list of students height ").split()
for n in range(0 , len(students_height)):
    students_height[n] = int(students_height[n])

 
print("\nCALCULATING AVERAGE HEIGHT OF FOLKS........")

total_height = 0
for height in students_height:
  total_height = total_height + height
  


total_students = 0
for student in students_height:
    total_students +=  1

    
avg = total_height / total_students

print(f"Average height of students in class is {avg}")