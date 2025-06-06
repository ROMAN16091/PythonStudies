from django.db import models

class Message(models.Model):
    text = models.CharField(max_length=225)

    def __str__(self):
        return self.text