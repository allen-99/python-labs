from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User
from .models import Movie, Genre, Category
from .forms import ReviewForm, ReviewGenreForm, ReviewCategoryForm, ReviewMovieForm
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt


class GenreV:

    def get_genres(self):
        return Genre.objects.all()

    def get_years(self):
        return Movie.objects.all().values("year")

    def get_category(self):
        return Category.objects.all()


class MoviesView(GenreV, ListView):
    model = Movie
    queryset = Movie.objects.all()
    template_name = 'movies/movie_list.html'


class MovieDetailView(GenreV, View):

    def get(self, request, slug):
        movie = Movie.objects.get(url=slug)
        return render(request, 'movies/movie.html', {'movie': movie})


class SendReview(View):

    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.movie = movie
            form.save()
        return redirect(movie.get_absolute_url())


class FilterMovieView(GenreV, ListView):

    def get_queryset(self):
        queryset = Movie.objects.filter(
            Q(year__in=self.request.GET.getlist("year")) |
            Q(genres__in=self.request.GET.getlist('genre')))
        return queryset


def AddMovie(request):
    if request.method == 'POST':
        form = ReviewMovieForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save()
            return redirect('/')

        return redirect('add_movie')

    if request.method == 'GET':
        categories = Category.objects.all()
        genres = Genre.objects.all()
        return render(request, 'add_movie.html', {'categories': categories, 'genres': genres})


class AddCategory(GenreV, View):
    def post(self, request):
        form = ReviewCategoryForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    def get(self, request):
        categories = Category.objects.all()
        return render(request, 'add_category.html', {'categories': categories})


class AddGenre(GenreV, View):

    def post(self, request):
        form = ReviewGenreForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    def get(self, request):
        genres = Genre.objects.all()
        return render(request, 'add_genre.html', {'genres': genres})
