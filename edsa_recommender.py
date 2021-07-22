"""

    Streamlit webserver-based Recommender Engine.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.

    NB: !! Do not remove/modify the code delimited by dashes !!

    This application is intended to be partly marked in an automated manner.
    Altering delimited code may result in a mark of 0.
    ---------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
    application. You are expected to extend certain aspects of this script
    and its dependencies as part of your predict project.

    For further help with the Streamlit framework, see:

    https://docs.streamlit.io/en/latest/

"""
# Streamlit dependencies
import streamlit as st

# Data handling dependencies
import pandas as pd
import numpy as np

# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model

# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')

# App declaration
def main():

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Recommender System","Data Summary","Solution Overview"]


    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.selectbox("Choose Option", page_options)
    if page_selection == "Recommender System":
        # Header contents
        st.write('# Movie Recommender Engine')
        st.write('### EXPLORE Data Science Academy Unsupervised Predict')
        st.image('resources/imgs/Image_header.png',use_column_width=True)
        # Recommender System algorithm selection
        sys = st.radio("Select an algorithm",
                       ('Content Based Filtering',
                        'Collaborative Based Filtering'))

        # User-based preferences
        st.write('### Enter Your Three Favorite Movies')
        movie_1 = st.selectbox('Fisrt Option',title_list[14930:15200])
        movie_2 = st.selectbox('Second Option',title_list[25055:25255])
        movie_3 = st.selectbox('Third Option',title_list[21100:21200])
        fav_movies = [movie_1,movie_2,movie_3]

        # Perform top-10 movie recommendation generation
        if sys == 'Content Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = content_model(movie_list=fav_movies,
                                                            top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


        if sys == 'Collaborative Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = collab_model(movie_list=fav_movies,
                                                           top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


    # -------------------------------------------------------------------

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------
    if page_selection == "Solution Overview":
        st.title("Solution Overview")
        st.write("Describe your winning approach on this page")

    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.
    if page_selection == "Data Summary":
        st.image("ratingsdistr.png")
        st.write("The distribution of the ratings indicate that most movies have a rating of atleast 3 and a rating of 4 is the most popular. The mean rating is around 3.5. This means that most of the movies in the dataset have a fairly good score. It also means that the ratings are skewed to the right which is proven by the mean and median calcualtion below. Further, it can inferred that based on the movies which are rated below 3, 15.4% of the movies in the dataset are 'bad' movies.")
        st.image("highratings.png")
        st.write("As expected, the higher the average ratings, the higher the number of ratings the movie has.")
        st.image("director.png")
        st.write("As expected, most directors with a high number of movies have average to good movie ratings. It would be great to determine if the ratings are affected by the year at which the ratings were made i.e. do the ratings decrease as the movie gets older? With changes in technology, audio and visuals are constantly improving. Due to this, people might give an older moviewith a low score as years progress as they would be comparing it with the current movies with better graphics.")
        st.image("plot.png")
        st.write("From the plot above, there is a slight drop from 1995 to 2020 in annual moving ratings howver it is not significant, at all. It seems as if the ratings given to a movie each year are not hugely affected by the year that the rating was given (there is no pattern in the ratings). From this, it can be concluded that the year of the rating has no significance in predicting the ratings of the movies. Movie duration can also be an important feature to consider when making a rating or when recommending a movie to someone as there might be viewers who do not like watching long movies or vice versa.")
        st.image("drama.png")
        st.write("Drama is the most common genre throughout the movies. Genres are important as they show the preferences of viewers and based on the genre that a viewer likes, movies of the same genre can be recommended. Movies in the dataset are associated with tags. The relevance of these tags is also provided.")

if __name__ == '__main__':
    main()
    