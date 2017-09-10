from django.db import models
import datetime
from django.utils import timezone


class Podcast(models.Model):
    """
        This class represents an episode.

    """

    def __str__(self):
        return "Title: " + self.title

    title = models.CharField(max_length=500)
    discription = models.CharField(max_length=1000)
    cover = models.CharField(max_length=500)
    podcast_id = models.IntegerField(default=0)

    nbr_episodes = models.IntegerField(default=0)
    nbr_episodes_played = models.IntegerField(default=0)

    last_refreshed = models.IntegerField(default=0)
    last_refreshed = models.IntegerField(default=0)


class Episode(models.Model):

    """
        This class represents an episode.
    """

    def __str__(self):
        return "Title: " + self.title

    def was_already_played(self):
        return times_played >= 1

    title = models.CharField(max_length=500)
    discription = models.CharField(max_length=1000)
    episode_id = models.IntegerField(default=0)

    duration = models.IntegerField(default=0)
    played_time = models.IntegerField(default=0)
    times_played = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')
    time = models.IntegerField(default=0)
