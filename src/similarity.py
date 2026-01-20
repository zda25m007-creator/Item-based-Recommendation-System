import math

def compute_cosine_similarity(
    movie_a,
    movie_b,
    movie_ratings_map,
    user_mean,
    min_common_users=10
):
    ratings_a = movie_ratings_map[movie_a]
    ratings_b = movie_ratings_map[movie_b]

    common_users = set(ratings_a.keys()) & set(ratings_b.keys())
    if len(common_users) < min_common_users:
        return 0.0

    num = denom_a = denom_b = 0.0

    for u in common_users:
        ra = ratings_a[u] - user_mean[u]
        rb = ratings_b[u] - user_mean[u]
        num += ra * rb
        denom_a += ra ** 2
        denom_b += rb ** 2

    if denom_a == 0 or denom_b == 0:
        return 0.0

    return num / math.sqrt(denom_a * denom_b)
