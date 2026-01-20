from collections import defaultdict

def generate_top_n_recommendations(
    user_id,
    user_ratings_map,
    movie_similarity_graph,
    user_mean_rating,
    N=10
):
    scores = defaultdict(float)
    sim_sums = defaultdict(float)

    rated_movies = user_ratings_map[user_id]
    user_mean = user_mean_rating[user_id]

    for rated_movie, rating in rated_movies.items():
        if rated_movie not in movie_similarity_graph:
            continue

        for sim_score, candidate_movie in movie_similarity_graph[rated_movie]:
            if candidate_movie in rated_movies:
                continue

            scores[candidate_movie] += sim_score * (rating - user_mean)
            sim_sums[candidate_movie] += abs(sim_score)

    predictions = []
    for movie in scores:
        if sim_sums[movie] > 0:
            predictions.append(
                (movie, user_mean + scores[movie] / sim_sums[movie])
            )

    predictions.sort(key=lambda x: x[1], reverse=True)
    return predictions[:N]
