# -*- coding: utf-8 -*-

from django.db import models


SOFTWARE_TYPE = (
("HUIYUAN","会员"),
("KUCUN","库存")
                 )
SERVE_TIME = (
("ONE MONTH", "一个月"),
("ONE YEAR","一年"),
("THREE YEAR","三年")
              )


class Software_service(models.Model):
    taobao_id = models.CharField("淘宝ID", max_length=200, blank=True)
    order_number = models.IntegerField("订单号", blank=True)
    offline_clients = models.CharField("线下客户", max_length=200, blank=True)
    credential = models.CharField("凭证", max_length=200, blank=True)
    remark = models.CharField("备注", max_length=200, blank=True)
    software_type = models.CharField("*软件类型", max_length=10, choices=SOFTWARE_TYPE,null=False,blank=False)
    serve_time = models.CharField("*服务时间", max_length=10, choices=SERVE_TIME,null=False,blank=False)


    def __unicode__(self):
        return self.taobao_id


