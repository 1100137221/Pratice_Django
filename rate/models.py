from django.db import models

# Create your models here.
class Rate(models.Model):
    countryName = models.TextField()
    buyCashRate = models.FloatField()
    sellCashRate = models.FloatField()
    buySpotRate = models.FloatField()
    sellSpotRate = models.FloatField()
    lastModifyDate = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "rate"