from django.db import models

class Position(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=200)

    def __str__(self):
        return self.name

class Candidate(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    birthdate = models.DateField()
    platform = models.TextField(max_length=200)

    def __str__(self):
        return self.lastname

class Vote(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name='can')
    vote_datetime = models.DateTimeField(auto_now=True)
