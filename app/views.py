
# from .request import get_movies,get_movie,search_movie
# from flask import render_template,request,redirect,url_for
from flask import render_template
from app import app
from .requests import get_movies
from .requests import get_movies,get_movie
# from .request import get_movies,get_movie,search_movie
from flask import render_template,request,redirect,url_for
# Views
@app.route('/')
def index():
   '''
   View root page function that returns the index page and its data
   '''
   # Getting popular movie
   popular_movies = get_movies('popular')
   upcoming_movie = get_movies('upcoming')
   now_showing_movie = get_movies('now_playing')
   title = 'Home - Welcome to The best Movie Review Website Online'
   return render_template('index.html', title = title, popular = popular_movies, upcoming = upcoming_movie, now_showing = now_showing_movie )
@app.route('/movie/<movie_id>')
def movie(movie_id):
   '''
   View movie page function that returns the movie details page and its data
   '''
   movie = get_movie(id)
   title = f'{movie_id}'
   return render_template('movie.html',title = title,movie = movie)
    