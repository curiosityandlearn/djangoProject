from django.shortcuts import render
from .forms import ServiceForm

# Create your views here.

def form_display(request):
    
    
    if request.method == "POST":
        form = ServiceForm(request.POST)
        form.save()

    form = ServiceForm()
    return render(request, 'formapp/form_display.html', {'form': form})
