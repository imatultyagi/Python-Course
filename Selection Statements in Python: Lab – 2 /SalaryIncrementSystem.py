# This program calculates the salary increment percentage for an employee based on their performance rating, years of experience, and attendance percentage.
performance_rating = int(input("Enter your performance rating (1-5): "))
#Performance rating validation  
if performance_rating < 1 or performance_rating > 5:
    print("Invalid performance rating. Please enter a value between 1 and 5.")
    exit(0) 
years_of_experience = int(input("Enter your years of experience: "))
#Years of experience validation
if years_of_experience < 0:
    print("Invalid years of experience. Please enter a positive value.")
    exit(0)
attendance_percentage = float(input("Enter your attendance percentage: "))
#Attendance percentage validation
if attendance_percentage < 0 or attendance_percentage > 100:
    print("Invalid attendance percentage. Please enter a value between 0 and 100.")
    exit(0)
#Increment calculation logic
increment_percentage = 0
if performance_rating == 5:
    increment_percentage += 10
elif performance_rating == 4:
    increment_percentage += 7
elif performance_rating == 3:
    increment_percentage += 5
if years_of_experience > 5:
    increment_percentage += 5
elif years_of_experience > 2:
    increment_percentage += 3
if attendance_percentage >= 95:
    increment_percentage += 5
elif attendance_percentage >= 90:
    increment_percentage += 3
print(f"Your total salary increment percentage is: {increment_percentage}%")


