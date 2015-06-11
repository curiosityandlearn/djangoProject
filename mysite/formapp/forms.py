from django import forms
from .models import Software_service

class ServiceForm(forms.ModelForm):

    class Meta:
        model = Software_service
        fields = ('taobao_id','ding_dan_hao','xian_xia_ke_hu','ping_ju')
