from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=225, null=True, blank=True)
    author = models.CharField(max_length=225, null=True, blank=True)
    subtitle = models.CharField(max_length=225, null=True, blank=True)
    isbn = models.CharField(max_length=225, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    