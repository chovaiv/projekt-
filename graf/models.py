from django.db import models

class Test(models.Model):
    jmeno_objektu = models.CharField(max_length=200)
    pocet_objektu = models.IntegerField()

    def __str__(self):
        return "{}-{}".format(self.jmeno_objektu, self.pocet_objektu)

    verbose_name_plural = "Testy"