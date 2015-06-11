from django.db import models

# Create your models here.

class Software_service(models.Model):
    taobao_id = models.CharField(max_length=200, blank=True)
    ding_dan_hao = models.IntegerField(blank=True)
    xian_xia_ke_hu = models.CharField(max_length=200, blank=True)
    ping_ju = models.CharField(max_length=200, blank=True)


    def __unicode__(self):
        return self.taobao_id


class A_second(models.Model):
    taobao_id = models.CharField(max_length=200)
    ding_dan_hao = models.IntegerField()

    def __unicode__(self):
        return self.taobao_id
