from django.db import models
from django.contrib.auth.models import User
from card.models import Card

class UserModel(User):
    cards = models.ManyToManyField(Card, blank=True)
    balance = models.IntegerField(default=5000)

    def __str__(self):
        return f'{self.username}' 
