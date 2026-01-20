def compute_user_mean_ratings(user_ratings_map):
    user_mean_rating = {}
    for user, ratings in user_ratings_map.items():
        user_mean_rating[user] = sum(ratings.values()) / len(ratings)
    return user_mean_rating
