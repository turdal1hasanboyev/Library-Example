from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, null=True, blank=True)
    subtitle = models.CharField(max_length=225, null=True, blank=True)
    isbn = models.CharField(max_length=225, null=True, blank=True)

    def __str__(self):
        return self.title
    