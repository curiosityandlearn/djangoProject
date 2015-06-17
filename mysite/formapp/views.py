from django.shortcuts import render
from models import Software_service
from .forms import ServiceForm
from django.http.response import HttpResponse


def form_input(request):
       
    if request.method == "POST":
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return HttpResponse("invalid input")
    form = ServiceForm
    return render(request, 'formapp/form_input.html', {'form': form})


def data_inquiry(request):
    query_results = Software_service.objects.all()
    return render(request, 'formapp/data_inquiry.html', {'query_results':query_results})