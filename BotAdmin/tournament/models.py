from django.db import models

class TournamentModel(models.Model):
    name = models.CharField(verbose_name="Название турнира", max_length=256)
