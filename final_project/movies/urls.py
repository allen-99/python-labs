from django.urls import path
from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.MoviesView.as_view()),
    path('filter/', views.FilterMovieView.as_view(), name='filter'),
    path('add_movie/', views.AddMovie, name='add_movie'),
    path('add_category/', views.AddCategory.as_view(), name='add_category'),
    path('add_genre/', views.AddGenre.as_view(), name='add_genre'),
    path('<slug:slug>/', views.MovieDetailView.as_view(), name='movie'),
    path('review/<int:pk>/', views.SendReview.as_view(), name='add_review'),

]
