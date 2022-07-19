from django.db import models

class emp(models.Model):
    First_Name=models.CharField(max_length=30)
    Last_Name=models.CharField(max_length=40)
    Age=models.IntegerField()
    Email=models.EmailField(max_length=30)
    Mob=models.BigIntegerField()
    Adress=models.CharField(max_length=50)

    def __str__(self):
        return self. First_Name