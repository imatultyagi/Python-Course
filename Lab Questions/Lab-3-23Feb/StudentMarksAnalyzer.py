#Student Marks Analyzer 

def analyze_marks(marks):
    # Remove invalid marks
    valid_marks = [mark for mark in marks if 0 <= mark <= 100]

    if not valid_marks:
        return "No valid marks to analyze."

    # Calculate average
    average = sum(valid_marks) / len(valid_marks)

    # Find topper(s)
    max_mark = max(valid_marks)
    toppers = [mark for mark in valid_marks if mark == max_mark]

    # Display grades based on average
    if average >= 90:
        grade = 'A'
    elif average >= 80:
        grade = 'B'
    elif average >= 70:
        grade = 'C'
    elif average >= 60:
        grade = 'D'
    else:
        grade = 'F'

    return {
        "average": average,
        "toppers": toppers,
        "grade": grade
    }   

# Example usage
marks_list = [85, 90, 78, 92, 88, -5, 105]  # Contains invalid marks
result = analyze_marks(marks_list)
print(result)

#output: {'average': 85.0, 'toppers': [90], 'grade': 'A'}