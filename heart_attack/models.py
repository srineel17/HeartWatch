from django.db import models

class Storedata(models.Model):
    fullname = models.CharField(max_length = 250)
    age = models.IntegerField()
    sex = models.IntegerField()
    cp_type = models.IntegerField()
    trest_bps = models.IntegerField()
    chol = models.IntegerField()
    fbs = models.IntegerField()
    rer = models.IntegerField()
    thalch = models.IntegerField()
    eia = models.IntegerField()
    oldpeak = models.FloatField()
    slope = models.IntegerField()
    ca = models.IntegerField()
    thal = models.IntegerField()




class Tempstorage(models.Model):
    name = models.CharField(max_length = 200)
    age = models.IntegerField()
