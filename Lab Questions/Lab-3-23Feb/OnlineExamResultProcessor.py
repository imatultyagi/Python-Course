#Online Exam Result Processor 

def process_exam_results(scores):
    if len(scores) <= 2:
        return "Not enough scores to process."

    # Remove lowest 2 scores
    sorted_scores = sorted(scores)
    valid_scores = sorted_scores[2:]

    # Add grace marks of 5 to those scoring between 30–35
    processed_scores = []
    for score in valid_scores:
        if 30 <= score < 35:
            processed_scores.append(score + 5)
        else:
            processed_scores.append(score)

    # Count number of students passed (≥ 40)
    passed_students = sum(1 for score in processed_scores if score >= 40)

    return {
        "processed_scores": processed_scores,
        "passed_students": passed_students
    }
# Example usage
exam_scores = [25, 30, 32, 28, 40, 45, 50]  # Contains scores to be processed
result = process_exam_results(exam_scores)
print(result)
#output: {'processed_scores': [35, 40, 45, 50],
