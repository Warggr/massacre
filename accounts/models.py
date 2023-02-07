from django.contrib.auth.models import AbstractUser
from django.db import models
from django.shortcuts import reverse

class User(AbstractUser):
    def get_absolute_url(self):
        return reverse('user_detail', kwargs={'pk': self.id})
