from django.db import models
from django.contrib.auth.models import User


class Game (models.Model):
    name = models.CharField(max_length=50)
    archetype = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    edition = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    age_min = models.IntegerField()
    age_max = models.IntegerField()
    player_min = models.IntegerField()
    player_max = models.IntegerField()
    time = models.IntegerField()  # Duration in minute
    language = models.CharField(max_length=50)  # Langue dispo pour le jeu
    description = models.TextField(500)
    picture = models.ImageField(upload_to="game")

    def __unicode__(self):
        return self.name


class Comment(models.Model):
    game_id = models.ForeignKey(Game)
    user_id = models.ForeignKey(User)
    comment = models.TextField(200)
    date_comment = models.DateField()
    time_comment = models.TimeField()
    date_comment.auto_now
    time_comment.auto_now
    cotation = models.SmallIntegerField()
    IPv4 = models.IPAddressField()
    IPv6 = models.IPAddressField()

    def __unicode__(self):
        return self.name


