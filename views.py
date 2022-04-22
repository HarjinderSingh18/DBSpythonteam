from django.shortcuts import redirect, render
from django.http import HttpResponse
from admin_panel.functions import *
from admin_panel.models import Admin
from app.models import Actor, Director, Movie, Genre
# Create your views here.

SALT = "AS^6dabBY*7ATs&*gASG6"

def dashboard(request):
    try:
        print(request.COOKIES["admin_session"])
    except KeyError:
        return redirect("login")
    actors = Actor.objects.all()
    movies = Movie.objects.all()
    return render(request,"admin_dashboard.html",{"title":"Admin | Dashboard","movies":movies,"actors":actors})

def logout(request):
    response = redirect("login")
    response.delete_cookie("admin_session")
    return response

def login(request):
    if request.method == "GET":
        return render(request,"admin_login.html",{"title":"Admin | Login"})
    if request.method == "POST":
        try:
            admin_id = Admin.objects.filter(username=request.POST["username"],password=request.POST["password"])[0].pk
        except IndexError:
            return render(request,"admin_login.html",{"title":"Admin | Login"})    
        
        response = redirect("dashboard")
        response.set_cookie("admin_session",str(admin_id)+"||"+SALT)
        return response

def movie(request,movie_id=None):
    try:
        print(request.COOKIES["admin_session"])
    except KeyError:
        return redirect("login")
    if movie_id != None:
        Movie.objects.filter(pk=movie_id).delete()
        return dashboard(request)

    if request.method == "GET":
        genre = Genre.objects.all()
        actors = Actor.objects.all()
        directors = Director.objects.all()
        return render(request,"add_movie.html",{"title":"Admin | Movie","genre":genre,"directors":directors,"actors":actors})
    if request.method == "POST":
        movie_data = {
            "director_id":request.POST["director"],
            "movie_title":request.POST["title"],
            "genres":request.POST.getlist("genres"),
            "actors":request.POST.getlist("actors"),
            "movie_type":request.POST["type"],
            "release_date":request.POST["date"],
            "duration":request.POST["duration"],
            "description":request.POST["description"]
        }
        addMovie(movie_data)
        return dashboard(request)

def actor(request,actor_id=None):
    try:
        print(request.COOKIES["admin_session"])
    except KeyError:
        return redirect("login")
    if actor_id != None:
        Actor.objects.filter(pk=actor_id).delete()
        return dashboard(request)

    if request.method == "GET":
        return render(request,"add_actor.html",{"title":"Admin | Actor"})
    if request.method == "POST":
        actor_data = {
            "name":request.POST["name"],
            "actor_type":request.POST["type"],
            "gender":request.POST["gender"],
            "age":request.POST["age"],
            "bio":request.POST["bio"],
            "other_details":request.POST["other_details"]
        }
        addActor(actor_data)
        return dashboard(request)