import pandas as pd
import numpy as np

# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model

# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')
movie_1 = title_list[14930:15200]
movie_2 = title_list[25055:25255]
movie_3 = title_list[21100:21200]
fav_movies = [movie_1,movie_2,movie_3]
top_recommendations = collab_model(movie_list=fav_movies,top_n=10)
print(top_recommendations)