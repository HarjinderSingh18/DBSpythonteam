from django.db import models

# Create your models here.
class Genre(models.Model):
    genre_name = models.CharField(max_length=255)

    def __str__(self):
        return self.genre_name

class Director(models.Model):
    director_name = models.CharField(max_length=255)

    def __str__(self):
        return self.director_name

class Actor(models.Model):
    name = models.CharField(max_length=255)
    actor_type = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    age = models.IntegerField()
    bio = models.CharField(max_length=255)
    other_details = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Movie(models.Model):
    director = models.ForeignKey(Director,on_delete=models.CASCADE)
    movie_title = models.CharField(max_length=255)
    movie_type = models.CharField(max_length=10)
    release_date = models.DateField()
    duration = models.CharField(max_length=10)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.movie_title

class User(models.Model):
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)
    age = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.username

class IMDB_Rating(models.Model):
    imdb_rating = models.CharField(max_length=10)
    imdb_rating_description = models.CharField(max_length=255)

class Movie_Review(models.Model):
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE) 
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    imdb = models.ForeignKey(IMDB_Rating,on_delete=models.CASCADE)
    review_date = models.DateField()
    review_description = models.CharField(max_length=255)

class Ass_Genre_Movie(models.Model):
    genre = models.ForeignKey(Genre,on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)

class Ass_Actor_Movie(models.Model):
    actor = models.ForeignKey(Actor,on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)