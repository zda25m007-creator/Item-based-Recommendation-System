import time
from src.data_loader import load_and_preprocess
from src.rating_maps import build_rating_maps
from src.user_mean import compute_user_mean_ratings
from src.similarity_graph import build_movie_similarity_graph
from src.inspection import show_similar_movies
from src.recommendation import generate_top_n_recommendations
from src.evaluation import build_test_ground_truth, evaluate_model


train_df, test_df, movies_df = load_and_preprocess(
    "data/ratings.csv",
    "data/movies.csv"
)

print("Train size:", len(train_df))
print("Test size:", len(test_df))

user_ratings_map, movie_ratings_map = build_rating_maps(train_df)

print("Number of users:", len(user_ratings_map))
print("Number of movies:", len(movie_ratings_map))

sample_user = next(iter(user_ratings_map))
sample_movie = next(iter(movie_ratings_map))

print("\nSample user:", sample_user)
print("Movies rated by user:", list(user_ratings_map[sample_user].items())[:5])

print("\nSample movie ID:", sample_movie)
print("Users who rated this movie:", list(movie_ratings_map[sample_movie].items())[:5])

user_mean_rating = compute_user_mean_ratings(user_ratings_map)

'''movie_similarity_graph = build_movie_similarity_graph(
    movie_ratings_map,
    user_mean_rating
)
'''
start_time = time.time()

movie_similarity_graph = build_movie_similarity_graph(
    movie_ratings_map,
    user_mean_rating
)

end_time = time.time()
print(
    "Similarity graph built in",
    round(end_time - start_time, 2),
    "seconds"
)

show_similar_movies(sample_movie, movie_similarity_graph, movies_df)

raw_recommendations = generate_top_n_recommendations(
    sample_user,
    user_ratings_map,
    movie_similarity_graph,
    user_mean_rating,
    N=20
)

print("\nTop-N Recommendations:")
movie_id_to_title = dict(zip(movies_df["movieId"], movies_df["title"]))
for movie_id, score in raw_recommendations[:5]:
    print(movie_id_to_title.get(movie_id), "| Score:", round(score, 3))

test_ground_truth = build_test_ground_truth(test_df)

metrics = evaluate_model(
    user_ratings_map,
    test_ground_truth,
    movie_similarity_graph,
    user_mean_rating,
    k=5
)


# ======================================================
# DEMO: RECOMMENDATIONS FOR A SPECIFIC USER
# ======================================================
user_id = 10

# Check if user exists
if user_id not in user_ratings_map:
    print(f"User {user_id} not found in training data.")
else:
    output = generate_top_n_recommendations(
        user_id,
        user_ratings_map,
        movie_similarity_graph,
        user_mean_rating,
        N=5
    )

    print("\nRecommendations for user:", user_id)
    for movie_id, score in output:
        print(
            movie_id_to_title.get(movie_id, "Unknown"),
            "| Predicted rating:",
            round(score, 3)
        )


print("\nEvaluation Metrics:")
print(metrics)
