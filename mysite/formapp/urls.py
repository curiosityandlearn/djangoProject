from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.form_input),
    url(r'^data_inquiry/$', views.data_inquiry),
    ]
