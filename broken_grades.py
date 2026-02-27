# Write a program that will average 3 numeric exam grades, return an average test score, a corresponding letter grade, and a message stating whether the student is passing.

# Average	Grade
# 90+	A
# 80-89	B
# 70-79	C
# 60-69	D
# 0-59	F

# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.

# Exams: 50, 51, 0
# Average: 33
# Grade: F
# Student is failing.

exam_one = int(input("Input exam grade one: "))

exam_two = int(input("Input exam grade two: ")) #add int before input

exam_three = int(input("Input exam grade three: ")) #replace str with int; replace exam_3 with exam_three

grades = [exam_one, exam_two, exam_three] #add commas after each variable

sum = 0
for grade in grades: #add s to grade 
  sum += grade #add + before = 

avg = sum / len(grades) #add a to grdes

if avg >= 90:
    letter_grade = "A"
elif avg >= 80 and avg < 90: #add : after 90
    letter_grade = "B"
elif avg >= 70 and avg < 80: #replace >69 with >= 70
    letter_grade = "C" #replace ' with " after C
elif avg >= 60 and avg < 70: #replace avg <= 69 with >=60; replace avg >= 65 with avg < 70
    letter_grade = "D" 
else: #replace elif with else
    letter_grade = "F"
    
for grade in grades:
    print("Exam: ", grade)

print("Average: ", round(avg)) #add round to avg, remove from loop for loop to prevent repetition in printing
print("Grade: ", letter_grade)

if letter_grade == "F": #replace is with ==, replace letter-grade with letter_grade
    print("Student is failing.") #add parenthesis, remove spacing
else:
    print("Student is passing.") #add parenthesis, remove spacing

