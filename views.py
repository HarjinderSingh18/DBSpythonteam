from email import message
from django.http import HttpResponse
from django.shortcuts import redirect, render
from app.functions import *
from app.models import *

# Create your views here.
SALT = "D&asf5^rsd6arf"

def login(request):
    if request.method == "GET":
        return render(request,"login.html",{"title":"IMDB | Login"})
    if request.method == "POST":
        if User.objects.filter(username=request.POST["username"]).count() == 0:
            message = "Username Not Found!"
            return render(request,"login.html",{"title":"IMDB | Login","message":message})
        elif User.objects.filter(username=request.POST["username"])[0].password != request.POST["password"]:
            message = "Incorrect Password!"
            return render(request,"login.html",{"title":"IMDB | Login","message":message})
        elif User.objects.filter(username=request.POST["username"],password=request.POST["password"]).count() != 0:
            user_id = User.objects.filter(username=request.POST["username"],password=request.POST["password"])[0].id
            response = redirect("home")
            response.set_cookie("user_session",str(user_id)+"||"+SALT)
            return response

def register(request):
    if request.method == "GET":
        return render(request,'register.html',{"title":"IMDB | Register"})
    if request.method == "POST":
        if User.objects.filter(username=request.POST["username"]).count() != 0:
            message = "Username Already Exists!"
            return render(request,"register.html",{"title":"IMDB | Register","message":message})
        else:
            user_data = {
                "name":request.POST["name"],
                "gender":request.POST["gender"],
                "age":request.POST["age"],
                "email":request.POST["email"],
                "address":request.POST["address"],
                "username":request.POST["username"],
                "password":request.POST["password"],
            }
            createUser(user_data)
            message = "Registration Successful."
            return render(request,"register.html",{"title":"IMDB | Register","message":message})

def home(request):
    try:
        cookie = request.COOKIES["user_session"]
        logged_in = True
    except KeyError:
        logged_in = False

    movies = Movie.objects.all()
    return render(request,"home.html",{"title":"IMDB | Home","logged_in":logged_in,"movies":movies})

def logout(request):
    response = redirect("login")
    response.delete_cookie("user_session")
    return response

def movie(request,movie_id):
    movie_data = Movie.objects.get(pk=movie_id)
    movie = Movie.objects.get(pk=movie_id)
    genres = Ass_Genre_Movie.objects.filter(movie=movie_id)
    actors = Ass_Actor_Movie.objects.filter(movie=movie_id)
    all_reviews = Movie_Review.objects.filter(movie=movie)
    user = False

    try:
        cookie = request.COOKIES["user_session"]
        user_id = cookie.split("||")[0]
        user = User.objects.get(pk=user_id)

        if Movie_Review.objects.filter(movie=movie,user=user).count() != 0:
            reviewed = True
        else:
            reviewed = False
    except KeyError:
        pass
    
    if request.method == "GET":
        return render(request,"movie.html",{"user":user,"reviewed":reviewed,"title":movie_data.movie_title,"movie":movie_data,"genres":genres,"actors":actors,"review_data":all_reviews})
    if request.method == "POST":
        try:
            cookie = request.COOKIES["user_session"]
            user_id = cookie.split("||")[0]
            user = User.objects.get(pk=user_id)
        except KeyError:
            return redirect('login')
        
        review_data = {
            "rating":request.POST["rating"],
            "review_title":request.POST["review_title"],
            "review":request.POST["review"],
            "user_id":user_id,
            "movie_id":movie_id,
        }
        
        
        if Movie_Review.objects.filter(movie=movie,user=user).count() != 0:
            reviewed = True
            return render(request,"movie.html",{"user":user,"reviewed":reviewed,"title":movie_data.movie_title,"movie":movie_data,"genres":genres,"actors":actors,"review_data":all_reviews})
        else:
            makeReview(review_data)
            reviewed = True
            return render(request,"movie.html",{"user":user,"reviewed":reviewed,"title":movie_data.movie_title,"movie":movie_data,"genres":genres,"actors":actors,"review_data":all_reviews})

def delete(request,review_id):
    try:
        cookie = request.COOKIES["user_session"]
        user_id = cookie.split("||")[0]
        user = User.objects.get(pk=user_id)
        review = Movie_Review.objects.get(pk=review_id,user=user)
        movie_id = review.movie.id
        review.delete()
    except :
        return redirect('login')

    movie_data = Movie.objects.get(pk=movie_id)
    movie = Movie.objects.get(pk=movie_id)
    genres = Ass_Genre_Movie.objects.filter(movie=movie_id)
    actors = Ass_Actor_Movie.objects.filter(movie=movie_id)
    all_reviews = Movie_Review.objects.filter(movie=movie)
    user = False

    try:
        cookie = request.COOKIES["user_session"]
        user_id = cookie.split("||")[0]
        user = User.objects.get(pk=user_id)
        if Movie_Review.objects.filter(movie=movie,user=user).count() != 0:
            reviewed = True
        else:
            reviewed = False
    except KeyError:
        pass

    return render(request,"movie.html",{"user":user,"reviewed":reviewed,"title":movie_data.movie_title,"movie":movie_data,"genres":genres,"actors":actors,"review_data":all_reviews})
