from django.db import models


SEX_CHOICES=(
('male','nan'),
('female','nv')
)

class Software_service(models.Model):
    taobao_id = models.CharField("TaoBao", max_length=200, blank=True)
    ding_dan_hao = models.IntegerField(blank=True)
    xian_xia_ke_hu = models.CharField(max_length=200, blank=True)
    ping_ju = models.CharField(max_length=200, blank=True)
    sex = models.CharField(max_length=10, choices=SEX_CHOICES,null=True,blank=True)


    def __unicode__(self):
        return self.taobao_id


