from django.urls import path
from admin_panel import views

urlpatterns = [
    path('dashboard/', views.dashboard, name="dashboard"),
    path('', views.login, name="login"),
    path('movie/', views.movie, name="movie"),
    path('actor/', views.actor, name="actor"),
    path('movie/<int:movie_id>', views.movie, name="movie"),
    path('actor/<int:actor_id>', views.actor, name="actor"),
    path('logout/', views.logout, name="logout")
]