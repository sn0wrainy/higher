from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Candidate(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)

    def __str__(self):
        return self.first_name + self.last_name


class Recruiter(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)

    def __str__(self):
        return self.first_name + self.last_name


class Task(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Grade(models.Model):
    value = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    recruiter = models.ForeignKey(Recruiter, on_delete=models.CASCADE)
