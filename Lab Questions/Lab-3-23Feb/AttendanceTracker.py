#Attendance Tracker

def analyze_attendance(attendance):
    total_classes = len(attendance)
    if total_classes == 0:
        return "No attendance data to analyze."

    # Calculate attendance percentage
    present_count = sum(attendance)
    attendance_percentage = (present_count / total_classes) * 100

    # Identify students below 75%
    if attendance_percentage < 75:
        status = "Below 75%"
    else:
        status = "Satisfactory"

    # Replace consecutive absences with a warning flag
    analyzed_attendance = []
    consecutive_absences = 0
    for day in attendance:
        if day == 0:  # Absent
            consecutive_absences += 1
            if consecutive_absences >= 3:
                analyzed_attendance.append("Warning: Consecutive Absences")
            else:
                analyzed_attendance.append(0)
        else:  # Present
            consecutive_absences = 0
            analyzed_attendance.append(1)

    return {
        "attendance_percentage": attendance_percentage,
        "status": status,
        "analyzed_attendance": analyzed_attendance
    }