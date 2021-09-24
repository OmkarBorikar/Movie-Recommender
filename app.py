import streamlit as st
import pickle
import pandas as pd
import requests
st.set_page_config(layout="wide")
# st.title('Movie Recommender Sysytem')
st.markdown("<h1 style='text-align: center; color: red;'>Movie Recommender System</h1>", unsafe_allow_html=True)


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    recommended_movie_names = []
    recommended_movie_posters=[]
    recommended_movie_overview = []
    recommended_movie_runtime = []
    recommended_movie_status = []
    recommended_movie_rating= []
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)
        recommended_movie_overview.append(movies.iloc[i[0]].overviw_og)
        recommended_movie_runtime.append(movies.iloc[i[0]].runtime)
        recommended_movie_status.append(movies.iloc[i[0]].status)
        recommended_movie_rating.append(movies.iloc[i[0]].vote_average)
    return recommended_movie_names,recommended_movie_posters,recommended_movie_overview,recommended_movie_runtime,recommended_movie_status,recommended_movie_rating


similarity = pickle.load(open('similarity.pkl','rb'))

movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

col6,col7,col8 = st.columns(3)
with col7:
    # select_label = '<p style="font-family:Courier; color:Blue; font-size: 20px;">Select the movie</p>'
    # lab = st.markdown(select_label,unsafe_allow_html=True)
    input = st.selectbox(label='Select the movie',options = movies['title'])
    butt = st.button('Show Recommendation')
    




if butt:
    recommended_movie_names,recommended_movie_posters,recommended_movie_overview,recommended_movie_runtime,recommended_movie_status,recommended_movie_rating= recommend(input)
    col1, col2,col3,col4,col5 = st.columns(5)
    # with col1:
    #     st.text(recommended_movie_names[0])
    #     st.image(recommended_movie_posters[0])
    # with col2:
    #     st.text(recommended_movie_names[1])
    #     st.image(recommended_movie_posters[1])

    # with col3:
    #     st.text(recommended_movie_names[2])
    #     st.image(recommended_movie_posters[2])
    # with col4:
    #     st.text(recommended_movie_names[3])
    #     st.image(recommended_movie_posters[3])
    # with col5:
    #     st.text(recommended_movie_names[4])
    #     st.image(recommended_movie_posters[4])
    # with col1:
    #     st.header(recommended_movie_names[0])
    #     st.markdown(recommended_movie_overview[0])
    #     st.text(recommended_movie_runtime[0])
    #     st.text(recommended_movie_status[0])
    #     st.text(recommended_movie_rating[0])

    # with col2:
    #     st.image(recommended_movie_posters[0])
    # with col1:
    #     st.header(recommended_movie_names[1])
    #     st.markdown(recommended_movie_overview[1])
    #     st.text(recommended_movie_runtime[1])
    #     st.text(recommended_movie_status[1])
    #     st.text(recommended_movie_rating[1])
    # with col2:
    #     st.image(recommended_movie_posters[1])
    # with col1:
    #     st.header(recommended_movie_names[2])
    #     st.markdown(recommended_movie_overview[2])
    #     st.text(recommended_movie_runtime[2])
    #     st.text(recommended_movie_status[2])
    #     st.text(recommended_movie_rating[2])
    # with col2:
    #     st.image(recommended_movie_posters[2])
    # with col1:
    #     st.header(recommended_movie_names[3])
    #     st.markdown(recommended_movie_overview[3])
    #     st.text(recommended_movie_runtime[3])
    #     st.text(recommended_movie_status[3])
    #     st.text(recommended_movie_rating[3])
    # with col2:
    #     st.image(recommended_movie_posters[3])
    # with col1:
    #     st.header(recommended_movie_names[4])
    #     st.markdown(recommended_movie_overview[4])
    #     st.text(recommended_movie_runtime[4])
    #     st.text(recommended_movie_status[4])
    #     st.text(recommended_movie_rating[4])
    # with col2:
    #     st.image(recommended_movie_posters[4])
    
    with col1:
        st.header(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
        st.markdown(recommended_movie_overview[0])
        st.text(recommended_movie_runtime[0])
        st.text(recommended_movie_status[0])
        st.text(recommended_movie_rating[0])

    with col2:
        st.header(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])
        st.markdown(recommended_movie_overview[1])
        st.text(recommended_movie_runtime[1])
        st.text(recommended_movie_status[1])
        st.text(recommended_movie_rating[1])
         
    with col3:
        st.header(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
        st.markdown(recommended_movie_overview[2])
        st.text(recommended_movie_runtime[2])
        st.text(recommended_movie_status[2])
        st.text(recommended_movie_rating[2])

    with col4:
        st.header(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
        st.markdown(recommended_movie_overview[3])
        st.text(recommended_movie_runtime[3])
        st.text(recommended_movie_status[3])
        st.text(recommended_movie_rating[3])

    with col5:
        st.header(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
        st.markdown(recommended_movie_overview[4])
        st.text(recommended_movie_runtime[4])
        st.text(recommended_movie_status[4])
        st.text(recommended_movie_rating[4])

    # with col1:

    # with col1:

    # with col1:

    # with col1:

    # with col1:         
    


