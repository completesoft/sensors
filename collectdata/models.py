from django.db import models

class Datastring(models.Model):
    add_date = models.DateTimeField('Добавлено', auto_now_add=True)
    devid = models.CharField('ID устройства', max_length=255, null=True, blank=True)
    temp = models.CharField('Температура', max_length=255, null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.devid)


class DataSDM(models.Model):
    add_date = models.DateTimeField('DATETIME', auto_now_add=True)
    devid = models.CharField('DEVID', max_length=255, null=True, blank=True)
    val1 = models.IntegerField('PHASE-1', null=True, blank=True)
    val2 = models.IntegerField('PHASE-2', null=True, blank=True)
    val3 = models.IntegerField('PHASE-3', null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.devid)


