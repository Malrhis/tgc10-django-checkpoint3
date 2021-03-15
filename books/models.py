from django.db import models

# Create your models here.


class Book(models.Model):
    # define a VARCHAR using Django
    title = models.CharField(blank=False, max_length=255)
    ISBN = models.CharField(blank=False, max_length=255)

    # TextField is the TEXT in MySQL (65000 characters)
    desc = models.TextField(blank=False)

    # define the relationship with the genre
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)

    # define the relationship with the tags
    tags = models.ManyToManyField('Tag')

    def __str__(self):
        return self.title


class Publisher(models.Model):
    name = models.CharField(blank=False, max_length=200)
    email = models.EmailField(blank=False, max_length=320)

    # toString function
    def __str__(self):
        return self.name + " (" + self.email + ")"


class Genre(models.Model):
    title = models.CharField(blank=False, max_length=255)

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(blank=False, max_length=255)

    def __str__(self):
        return self.title
