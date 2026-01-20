def show_similar_movies(sample_movie, movie_similarity_graph, movies_df):
    movie_id_to_title = dict(zip(movies_df["movieId"], movies_df["title"]))

    print("Sample movie ID:", sample_movie)
    print("Sample movie title:", movie_id_to_title.get(sample_movie, "Unknown"))

    print("\nTop similar movies:")
    for sim_score, movie_id in movie_similarity_graph[sample_movie][:5]:
        print(
            f"Similarity: {round(sim_score, 3)} | "
            f"Movie ID: {movie_id} | "
            f"Title: {movie_id_to_title.get(movie_id)}"
        )
