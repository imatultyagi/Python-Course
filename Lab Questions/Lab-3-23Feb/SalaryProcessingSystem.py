#Salary Processing System 

def process_salaries(salaries, minimum_wage):
    # Remove salaries below minimum wage
    valid_salaries = [salary for salary in salaries if salary >= minimum_wage]

    # Add 5% bonus to employees with salary > 50,000
    processed_salaries = []
    for salary in valid_salaries:
        if salary > 50000:
            salary *= 1.05  # Add 5% bonus
        processed_salaries.append(salary)

    # Sort salaries in descending order
    processed_salaries.sort(reverse=True)

    # Display top 3 highest salaries
    top_salaries = processed_salaries[:3]

    return top_salaries
# Example usage
salaries_list = [45000, 55000, 60000, 30000, 70000]  # Contains a salary below minimum wage
minimum_wage = 40000
top_salaries = process_salaries(salaries_list, minimum_wage)
print(f"Top 3 highest salaries: {top_salaries}")
#output: Top 3 highest salaries: [73500.0, 63000.0, 45000]

