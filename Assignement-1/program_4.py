#Question:  Use the if statement conditions to write a program to print the letter grade based on an input class score. Use the grading scheme we are using in this class. 


# Enter the score 
class_score = float(input("Enter the class score: "))

# Grade based on the class score 

if 90 <= class_score <= 100:
    grade = 'A'
elif 80 <= class_score < 90:
    grade = 'B'
elif 70 <= class_score < 80:
    grade = 'C'
elif 60 <= class_score < 70:
    grade = 'D'
else:
    grade = 'F'

# Print the grade
print("The Grade for the class score ",class_score," is: ",grade)
