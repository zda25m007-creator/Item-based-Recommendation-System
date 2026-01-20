import pandas as pd
import numpy as np

def load_and_preprocess(ratings_path, movies_path, test_ratio=0.2, seed=42):
    ratings_df = pd.read_csv(ratings_path)
    movies_df = pd.read_csv(movies_path)

    ratings_df.dropna(inplace=True)
    ratings_df.drop_duplicates(inplace=True)

    np.random.seed(seed)
    mask = np.random.rand(len(ratings_df)) < (1 - test_ratio)

    train_df = ratings_df[mask]
    test_df = ratings_df[~mask]

    return train_df, test_df, movies_df
