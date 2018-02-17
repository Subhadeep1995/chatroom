from django.db import models
from django.contrib.auth.models import User

class Chatroom(models.Model):
    name = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User)

    def __str__(self):
        return self.name

class Message(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User)
    chatroom = models.ForeignKey(Chatroom)

    def __str__(self):
        return self.text

