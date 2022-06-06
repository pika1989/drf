from django.db import models


class User(models.Model):

    MALE = 'm'
    FEMALE = 'f'
    SEX_CHOICES = [
        (MALE, 'male'),
        (FEMALE, 'female'),
    ]

    login = models.CharField(max_length=16, unique=True)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    birth_date = models.DateField()
    group = models.ForeignKey('Group', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.login


class Group(models.Model):
    name = models.CharField(max_length=16, unique=True)
    public = models.BooleanField(default=True)

    def __str__(self):
        return self.name