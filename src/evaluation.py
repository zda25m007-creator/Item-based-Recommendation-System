import math
from collections import defaultdict

def build_test_ground_truth(test_df, threshold=4.0):
    ground_truth = defaultdict(set)
    for _, row in test_df.iterrows():
        if row["rating"] >= threshold:
            ground_truth[int(row["userId"])].add(int(row["movieId"]))
    return ground_truth


def precision_at_k(recommended, relevant, k):
    return sum(1 for m in recommended[:k] if m in relevant) / k if recommended else 0


def recall_at_k(recommended, relevant, k):
    return sum(1 for m in recommended[:k] if m in relevant) / len(relevant) if relevant else 0


def ndcg_at_k(recommended, relevant, k):
    dcg = sum(
        1 / math.log2(i + 2)
        for i, m in enumerate(recommended[:k])
        if m in relevant
    )

    idcg = sum(1 / math.log2(i + 2) for i in range(min(len(relevant), k)))
    return dcg / idcg if idcg else 0


def evaluate_model(
    user_ratings_map,
    test_ground_truth,
    movie_similarity_graph,
    user_mean_rating,
    k=5,
    max_users=100
):
    precisions, recalls, ndcgs = [], [], []
    users = list(test_ground_truth.keys())[:max_users]

    for user_id in users:
        if user_id not in user_ratings_map:
            continue

        from src.recommendation import generate_top_n_recommendations

        recs = generate_top_n_recommendations(
            user_id,
            user_ratings_map,
            movie_similarity_graph,
            user_mean_rating,
            N=k
        )

        recommended_movies = [m for m, _ in recs]
        relevant_movies = test_ground_truth[user_id]

        if not relevant_movies:
            continue

        precisions.append(precision_at_k(recommended_movies, relevant_movies, k))
        recalls.append(recall_at_k(recommended_movies, relevant_movies, k))
        ndcgs.append(ndcg_at_k(recommended_movies, relevant_movies, k))

    return {
        "Precision@K": round(sum(precisions) / len(precisions), 6),
        "Recall@K": round(sum(recalls) / len(recalls), 6),
        "NDCG@K": round(sum(ndcgs) / len(ndcgs), 6),
    }
