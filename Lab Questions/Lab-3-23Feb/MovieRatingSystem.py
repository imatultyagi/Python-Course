#Movie Rating System

def analyze_movie_ratings(ratings):
    # Remove invalid ratings
    valid_ratings = [rating for rating in ratings if 1 <= rating <= 5]

    if not valid_ratings:
        return "No valid ratings to analyze."

    # Calculate average rating
    average_rating = sum(valid_ratings) / len(valid_ratings)

    # Count how many 5-star ratings
    five_star_count = valid_ratings.count(5)

    # Sort ratings in ascending order
    sorted_ratings = sorted(valid_ratings)

    return {
        "average_rating": average_rating,
        "five_star_count": five_star_count,
        "sorted_ratings": sorted_ratings
    }
# Example usage
movie_ratings = [5, 4, 3, 5, 2, 6, 0, 5]  # Contains valid and invalid ratings
result = analyze_movie_ratings(movie_ratings)
print(result)
#output: {'average_rating': 4.0, 'five_star_count': 3, 'sorted_ratings': [2, 3, 4, 5, 5, 5]}
