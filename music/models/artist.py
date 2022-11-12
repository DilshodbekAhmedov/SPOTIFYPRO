from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    picture = models.URLField(null=True)

    def __str__(self):
        return self.name

