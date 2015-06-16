from .models import Software_service
from django.forms import ModelForm

class ServiceForm(ModelForm):
    class Meta:
        model = Software_service
        fields = ['taobao_id','sex']
