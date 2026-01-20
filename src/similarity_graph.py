import heapq
from collections import defaultdict
from src.similarity import compute_cosine_similarity

def build_movie_similarity_graph(
    movie_ratings_map,
    user_mean_rating,
    min_similarity=0.1,
    top_k_neighbors=50,
    min_common_users=10
):
    similarity_graph = defaultdict(list)
    movie_ids = list(movie_ratings_map.keys())

    for i in range(len(movie_ids)):
        for j in range(i + 1, len(movie_ids)):
            sim = compute_cosine_similarity(
                movie_ids[i],
                movie_ids[j],
                movie_ratings_map,
                user_mean_rating,
                min_common_users
            )

            if sim >= min_similarity:
                similarity_graph[movie_ids[i]].append((sim, movie_ids[j]))
                similarity_graph[movie_ids[j]].append((sim, movie_ids[i]))

    for movie_id in similarity_graph:
        similarity_graph[movie_id] = heapq.nlargest(
            top_k_neighbors,
            similarity_graph[movie_id]
        )

    return similarity_graph
