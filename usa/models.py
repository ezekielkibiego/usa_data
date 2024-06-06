from django.db import models

class State(models.Model):
    state_name = models.CharField(max_length=100)
    state_abbrev = models.CharField(max_length=10)
    region = models.CharField(max_length=100)
    division = models.CharField(max_length=100)

    def __str__(self):
        return self.state_name
    

class Person(models.Model):
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    state_code = models.CharField(max_length=2, null=True)
    shirt_or_hat = models.CharField(max_length=100, null=True)
    quiz_points = models.IntegerField(null=True)
    team = models.CharField(max_length=100, null=True)
    signup = models.DateField(null=True)
    age = models.IntegerField(null=True)
    company = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
