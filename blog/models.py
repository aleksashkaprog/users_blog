import datetime

import django.utils.timezone
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models



class Post(models.Model):
    """
    Post model
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=20)
    text = models.TextField(max_length=140, blank=True)
    create_time = models.DateTimeField(default=django.utils.timezone.now)


    def __str__(self):
        return self.title


class Follower(models.Model):
    """
    Followers' model
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='owner'
    )
    subscriber = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='subscribers'
    )
