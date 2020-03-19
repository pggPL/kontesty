from django.db import models


# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    real_name = models.CharField(max_length=30)
    real_surname = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    school = models.CharField(max_length=30)
    password = models.CharField(max_length=80)
    user_class = models.IntegerField()
    admin = models.BooleanField(default=False)
    marks = models.CharField(max_length=30, default="")


class Settings(models.Model):
    contest_name = models.CharField(max_length=100)
    main_page_content = models.TextField()
    rules = models.TextField()
    number_of_problems = models.IntegerField()
    constest_start = models.DateTimeField()
    contest_duration_in_minutes = models.IntegerField()
    mark_view = models.BooleanField(default=False)


class Solutions(models.Model):
    username = models.CharField(max_length=30)
    problem_number = models.IntegerField()
    file_name = models.CharField(max_length=50, default="sol")
    file = models.FileField()
