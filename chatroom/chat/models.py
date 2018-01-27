from django.db import models

# Create your models here.
class session(models.Model):
    user_id = models.CharField(max_length = 1000)
    name = models.CharField(max_length = 1000)

    def __str__(self):
        return self.user_id
