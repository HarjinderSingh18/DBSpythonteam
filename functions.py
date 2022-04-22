from app.models import *
import datetime

def addMovie(movie_data):
    """
    This function recieve a python dictionary with all movie related data
    director_id, title, genre, type, date, duration, description
    """
    tmp_movie = Movie()
    tmp_movie.director = Director.objects.filter(pk=movie_data['director_id'])[0]
    tmp_movie.movie_title = movie_data['movie_title']
    tmp_movie.movie_type = movie_data['movie_type']
    tmp_movie.release_date = datetime.datetime.strptime(movie_data['release_date'],"%Y-%m-%d").date()
    tmp_movie.duration = movie_data['duration']
    tmp_movie.description = movie_data['description']
    tmp_movie.save()
    for i in movie_data['genres']:
        tmp_genre = Genre.objects.get(pk=i)
        Ass_Genre_Movie.objects.create(genre=tmp_genre,movie=tmp_movie)
    for i in movie_data["actors"]:
        tmp_actor = Actor.objects.get(pk=i)
        Ass_Actor_Movie.objects.create(actor=tmp_actor,movie=tmp_movie)

def addActor(actor_data):
    """
    This function recieve a python dictionary with all actor related data
    director_id, title, genre, type, date, duration, description
    """
    tmp_actor = Actor()
    tmp_actor.name = actor_data['name']
    tmp_actor.actor_type = actor_data['actor_type']
    tmp_actor.gender = actor_data['gender']
    tmp_actor.age = actor_data['age']
    tmp_actor.bio = actor_data['bio']
    tmp_actor.other_details = actor_data['other_details']
    tmp_actor.save()