# Question 1: Student Grades List (List - basic operations)
#Arnaldo Neto
grades = [85, 92, 78, 95, 88]

grades.append(90)
grades.sort()
print("Sorted grades:", grades)
print("Highest grades:", grades[-1])
print("Lowest grades:", grades[0])
print("Total number of grades:", len(grades))