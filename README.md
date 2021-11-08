# Movie-Recommender
Content based Movie recommendation system.

Dataset used for this project can be found here - [TMDB 5000 Movie dataset](https://www.kaggle.com/tmdb/tmdb-movie-metadata?select=tmdb_5000_movies.csv)

This project is deployed on Heroku and working web app can be accessed here - [Movie Recommender](https://tmdb-movie-recommender.herokuapp.com/)

# About Dataset - 

This dataset contains detailes information of around 5000 movies. Out of all features present in this dataset, features which are used for this project are - movie_id, title,genres, keywords, overview, cast, crew, runtime, status, vote_average.

![image](https://user-images.githubusercontent.com/82905366/140716109-d9ba6c3f-8ce7-48ec-91a5-ecea82941f2d.png)

# Web app Overview

After inputting movie and clicking 'Show Recommendation' Top 5 matching movies are displayed with their poster, Description, Release date and rating.

Web application can be accessed from here - [Movie Recommender](https://tmdb-movie-recommender.herokuapp.com/)

![image](https://user-images.githubusercontent.com/82905366/140718314-f5eee7ac-081f-4917-8f99-e110a4e2bb05.png)

# Tools and Libraries used for this project

Pandas and Numpy - For importing dataset and manipulating it in desired format for further use.

CountVecorizer and Cosine_similarity - Count vectorizer is used for vectorisation and cosine_similarity is used to measure cosine distance between these vectors.

Streamlit - Framework used to build this web application

Heroku - Web app is deployed on Heroku.

# Approach

* As stated earlier, out of all the features only selected features are considered for this project which are movie_id, title, genres, keywords, overview, cast, crew, runtime, status, vote_average.
* ast.literal_eval() is used to convert string to lists for columns genre, keywords, cast, crew.
* Created new column containg contents of genre, keywords, cast (Only first 3 casts), crew (Only director), overview.
* For each movie this newly created column named 'tags' is vectorised using Countvectorizer.
* Cosine similarity is used to measure cosine distance between each vector.
* When input movie is provided by the user, top 5 closest movie vectors are returned.



