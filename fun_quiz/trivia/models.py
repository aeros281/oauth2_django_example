from django.db import models


class Trivia(models.Model):
    """ Trivia model."""
    short_description = models.TextField()
    long_description = models.TextField()
