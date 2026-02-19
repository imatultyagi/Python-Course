# This program categorizes patients into triage categories based on their age, heart rate, and presence of severe injury.

age = int(input("Enter the patient's age: "))
# Age validation
if age < 0:
    print("Invalid age. Please enter a positive value.")
    exit(0)
heart_rate = int(input("Enter the patient's heart rate: "))
# Heart rate validation
if heart_rate < 0:
    print("Invalid heart rate. Please enter a positive value.")
    exit(0)
severe_injury = input("Does the patient have a severe injury? (yes/no): ").lower()
# Severe injury validation  
if severe_injury not in ["yes", "no"]:
    print("Invalid input for severe injury. Please enter yes or no.")
    exit(0)
# Triage categorization
if heart_rate < 60 or heart_rate > 100 or severe_injury == "yes":
    priority = "Critical"
elif age > 65:
    priority = "Moderate"
else:
    priority = "Normal"
print(f"The patient's triage category is: {priority}")
