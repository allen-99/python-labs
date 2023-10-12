from django import forms

from .models import Comment, Movie, Category, Genre


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('title', 'text')


class ReviewMovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['name', 'description', 'year', 'category', 'genres', 'photo', 'url']


class ReviewCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name', 'description')


class ReviewGenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ('name', 'description')