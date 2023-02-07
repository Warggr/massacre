from django.db import models
from django.shortcuts import reverse

class Team(models.Model):
    name = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('team_detail', args=[self.id])
