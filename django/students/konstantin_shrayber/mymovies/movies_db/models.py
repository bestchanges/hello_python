from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Person(models.Model):
    full_name = models.CharField(max_length=200)
    date_of_birth = models.DateTimeField('date of birth')
    country = models.CharField(max_length=30)


class HollywoodCompany(models.Model):
    title = models.CharField(max_length=30)


class Movie(models.Model):
    title = models.CharField(max_length=200)
    release_year = models.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2100)])
    budget = models.FloatField(validators=[MinValueValidator(100000), MaxValueValidator(1000000000)])
    director = models.ForeignKey(Person, on_delete=models.CASCADE)
    created_by = models.ForeignKey(HollywoodCompany, on_delete=models.CASCADE)


class Role(models.Model):
    movie_role = models.CharField(max_length=30)


class MovieCrew(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)