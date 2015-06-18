from .models import Software_service
from django.forms import ModelForm

class ServiceForm(ModelForm):
    class Meta:
        model = Software_service
        fields = ['taobao_id','order_number','offline_clients','credential',
                  'remark','software_type','serve_time',]
