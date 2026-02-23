#Sports Tournament Points Table

def analyze_tournament(points):
    if not points:
        return "No tournament data to analyze."

    # Replace negative points with 0
    cleaned_points = [max(0, point) for point in points]

    # Sort leaderboard
    sorted_points = sorted(cleaned_points, reverse=True)

    # Find winner and runner-up
    winner = sorted_points[0] if sorted_points else None
    runner_up = sorted_points[1] if len(sorted_points) > 1 else None

    return {
        "winner": winner,
        "runner_up": runner_up,
        "sorted_leaderboard": sorted_points
    }
# Example usage
team_points = [10, 20, -5, 15, 0, 25]  # Contains valid and invalid points
result = analyze_tournament(team_points)
print(result)
#output: {'winner': 25, 'runner_up': 20, 'sorted_leaderboard': [25, 20, 15, 10, 0, 0]}
