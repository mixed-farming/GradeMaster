from django.db import models
from django.core import validators


class Item(models.Model):

    SEX_CHOICES = (
        (1, 'male'),
        (2, 'female'),
    )

    name = models.CharField(
        verbose_name='name',
        max_length=200,
    )
    age = models.IntegerField(
        verbose_name='age',
        validators=[validators.MinValueValidator(1)],
        blank=True,
        null=True,
    )
    sex = models.IntegerField(
        verbose_name='sex',
        choices=SEX_CHOICES,
        default=1
    )
    memo = models.TextField(
        verbose_name='remarks',
        max_length=300,
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(
        verbose_name='registration date',
        auto_now_add=True
    )

    # Display settings on the administration site
    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name = 'item'
        verbose_name_plural = 'items'

class Document(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    file = models.FileField(upload_to='documents/')