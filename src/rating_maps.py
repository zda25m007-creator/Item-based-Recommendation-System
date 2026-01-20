from collections import defaultdict

def build_rating_maps(ratings_df):
    user_ratings_map = defaultdict(dict)
    movie_ratings_map = defaultdict(dict)

    for _, row in ratings_df.iterrows():
        user_id = int(row["userId"])
        movie_id = int(row["movieId"])
        rating = float(row["rating"])

        user_ratings_map[user_id][movie_id] = rating
        movie_ratings_map[movie_id][user_id] = rating

    return user_ratings_map, movie_ratings_map
