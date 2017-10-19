from django.db import models

# Create your models here.
class Weather(models.Model):
    countryName = models.TextField()
    type = models.TextField()
    info = models.TextField()
    temperature = models.TextField()
    img = models.TextField()
    date = models.TextField()
    lastModifyDate = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "weather"