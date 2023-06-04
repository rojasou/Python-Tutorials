# weighted exam score average

# entering number exams completed
num_of_exams = int(input("Enter number of exams: "))

# entering how many credits the exams cover
total_credits = int(input("Enter number of credits these exams cover: "))

# begin with average of 0 then add up percentages of exams
average = 0

# for loop takes in exam scores and calculates average
for exam in range(num_of_exams):
    score = int(input("Enter exam score: "))
    exam_credits = int(input("Enter how many credits this exam covered: "))
    average = average + score * exam_credits / total_credits
print("Your average is: ", average)
