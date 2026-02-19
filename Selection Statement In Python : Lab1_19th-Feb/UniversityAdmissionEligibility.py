# This program checks the eligibility of a student for admission based on their 12th grade percentage, whether they studied Mathematics, and their entrance exam score.
 
marksPercentage = float(input("Enter your 12th grade percentage: "))
#Marks validation
if marksPercentage < 0 or marksPercentage > 100:
    print("Invalid percentage. Please enter a value between 0 and 100.")
    exit(0)
#subject validation
studiedMath = input("Have you studied Mathematics? (yes/no): ").lower()
if studiedMath not in ["yes", "no"]:
    print("Invalid input for Mathematics. Please enter yes or no.")
    exit(0)
entranceScore = float(input("Enter your entrance exam score: "))
#Entrance score validation
if entranceScore < 0 or entranceScore > 100:
    print("Invalid entrance exam score. Please enter a value between 0 and 100.")
    exit(0)
#Eligibility check
if marksPercentage < 75 and studiedMath == "no" and entranceScore < 80:
    print("You are not eligible for admission because you did not meet the percentage requirement, did not study Mathematics, and did not achieve the required entrance exam score.")
else:    
    print("You are eligible for admission.")
