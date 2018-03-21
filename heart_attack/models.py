from django.db import models



class storedata(models.Model):
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
    slpe = models.IntegerField()
    ca = models.IntegerField()
    thal = models.IntegerField()
    ads = models.IntegerField()
