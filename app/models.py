from django.db import models

# Create your models here.
class emp(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=30)
    age=models.IntegerField()