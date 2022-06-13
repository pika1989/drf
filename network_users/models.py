from django.db import models

from .validators import NameValidator


class User(models.Model):

    MALE = 'male'
    FEMALE = 'female'
    SEX_CHOICES = [
        (MALE, 'male'),
        (FEMALE, 'female'),
    ]

    login = models.CharField(max_length=16, unique=True, validators=[NameValidator()])
    sex = models.CharField(max_length=6, choices=SEX_CHOICES)
    birth_date = models.DateField()

    def __str__(self):
        return self.login


class Group(models.Model):
    name = models.CharField(max_length=16, unique=True, validators=[NameValidator()])
    public = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Members(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    group = models.ForeignKey('Group', on_delete=models.CASCADE)