from curses.ascii import US
from app.models import *
import datetime

def createUser(user_data):
    tmp_user = User()
    tmp_user.name = user_data['name']
    tmp_user.gender = user_data['gender']
    tmp_user.age = user_data['age']
    tmp_user.email = user_data['email']
    tmp_user.address = user_data['address']
    tmp_user.username = user_data['username']
    tmp_user.password = user_data['password']
    tmp_user.save()

def makeReview(review_data):
    tmp_imdb = IMDB_Rating()
    tmp_imdb.imdb_rating = review_data["rating"]
    tmp_imdb.imdb_rating_description = review_data["review_title"]
    tmp_imdb.save()
    
    tmp_movie_review = Movie_Review()
    tmp_movie_review.imdb = tmp_imdb
    tmp_movie_review.review_date = datetime.datetime.now().date()
    tmp_movie_review.review_description = review_data["review"]
    tmp_movie_review.movie = Movie.objects.get(pk=review_data["movie_id"])
    tmp_movie_review.user = User.objects.get(pk=review_data["user_id"])
    tmp_movie_review.save()