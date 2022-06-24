from django.db import models


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
    rewiev = models.ForeignKey(
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
