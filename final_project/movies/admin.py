from django.contrib import admin
from .models import Category, Comment, Movie, Genre


admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Movie)
admin.site.register(Genre)

# Register your models here.
