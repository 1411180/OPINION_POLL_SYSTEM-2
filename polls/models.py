from django.db import models
from django.contrib.auth.models import User

class Poll(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    craeted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Question(models.Model):
    poll = models.ForeignKey(Poll, related_name='questions', on_delete=models.CASCADE)
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text

class Choice(models.Model):
    question = models.ForeignKey(Poll, related_name='questions', on_delete=models.CASCADE)
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text

class Vote(models.Model):
    poll = models.ForeignKey(Poll, related_name='votes', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vote_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("poll", "user")            