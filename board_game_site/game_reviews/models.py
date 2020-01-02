from django.db import models

class GameReview(models.Model):
    game_score = models.CharField(max_length=30)
    comment = models.CharField(max_length=30)
    game_photos = models.CharField(max_length=30)
    game_objects = models.CharField(max_length=30)
    game_rules = models.CharField(max_length=30)

class Comment(models.Model):
    id = models.CharField(max_length=30, primary_key = True)
    commenter = models.CharField(max_length=30)
    content = models.CharField(max_length=30)

