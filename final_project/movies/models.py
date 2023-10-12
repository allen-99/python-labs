from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField("Категория", max_length=100)
    description = models.TextField("Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Genre(models.Model):
    name = models.CharField("Жанр", max_length=100)
    description = models.TextField("Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Movie(models.Model):
    name = models.CharField("Фильм", max_length=100)
    description = models.TextField("Описание", default='')
    year = models.PositiveIntegerField("Год")
    genres = models.ManyToManyField(Genre,
                                    verbose_name='Жанры')
    category = models.ForeignKey(Category,
                                 max_length=100,
                                 verbose_name='Категории',
                                 null=True,
                                 on_delete=models.SET_NULL)
    photo = models.ImageField('Постер', upload_to='movies/')
    url = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("movie", kwargs={'slug': self.url})


    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'


class Comment(models.Model):
    user = models.CharField("Пользователь", max_length=100)
    title = models.CharField("Заголовок", max_length=200)
    text = models.TextField("Текст отзыва", max_length=5000)
    movie = models.ForeignKey(Movie, verbose_name='Фильм', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.movie} - {self.user}"

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


