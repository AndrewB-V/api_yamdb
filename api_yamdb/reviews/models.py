from django.db import models
from reviews.validators import validate_year
from users.models import User


class Category(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='Категория',
        help_text='Выберите категорию'
    )
    slug = models.SlugField(
        max_length=50,
        unique=True,
        verbose_name='Слаг',
        help_text='Укажите слаг'
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('-id',)

    def str(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='Жанр',
        help_text='Название жанра'
    )
    slug = models.SlugField(
        max_length=50,
        unique=True,
        verbose_name='Слаг',
        help_text='Укажите слаг'
    )

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
        ordering = ('-id',)

    def str(self):
        return self.name


class Title(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='Произведение',
        help_text='Введите название произведения',
        db_index=True
    )
    year = models.SmallIntegerField(
        verbose_name='Год выпуска',
        help_text='Введите год выпуска',
        validators=[validate_year],
        blank=True
    )
    description = models.TextField(
        verbose_name='Описание',
        help_text='Описание произведения',
        max_length=250,
        null=True,
        blank=True
    )
    genre = models.ManyToManyField(
        Genre,
        related_name='titles',
        verbose_name='Жанр',
        help_text='Укажите жанр'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='titles',
        verbose_name='Категория',
        help_text='Укажите категорию'
    )

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'
        ordering = ('-id',)

    def str(self):
        return self.name[:15]


class Review(models.Model):
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        max_length=200,
        related_name='reviews',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        max_length=50,
        related_name='reviews',
    )
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField()

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['-pub_date']
        constraints = [models.UniqueConstraint(
            fields=['title', 'author'],
            name='unique_review',
        )]


class Comment(models.Model):
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        max_length=200,
        related_name='comments',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        max_length=50,
        related_name='comments',
    )
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return f'{self.review}, {self.text}'
