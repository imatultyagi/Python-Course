#Temperature Monitoring System

def analyze_temperatures(temperatures):
    if not temperatures:
        return "No temperature data to analyze."

    # Find hottest and coldest day
    hottest_day = max(temperatures)
    coldest_day = min(temperatures)

    # Replace temperatures above 45°C with “Heat Alert”
    analyzed_temperatures = []
    extreme_days_count = 0
    for temp in temperatures:
        if temp > 45:
            analyzed_temperatures.append("Heat Alert")
            extreme_days_count += 1
        else:
            analyzed_temperatures.append(temp)

    return {
        "hottest_day": hottest_day,
        "coldest_day": coldest_day,
        "analyzed_temperatures": analyzed_temperatures,
        "extreme_days_count": extreme_days_count
    }
# Example usage
temperature_list = [30, 35, 40, 42, 46, 38, 28, 50]  # Contains daily temperatures
result = analyze_temperatures(temperature_list)
print(result)
#output: {'hottest_day': 50, 'coldest_day': 28, 'analyzed_temperatures': [30, 35, 40, 42, 'Heat Alert', 38, 28, 'Heat Alert'], 'extreme_days_count': 2}
