from django.shortcuts import render
from .models import Portafolio

# Create your views here.
def portafolio(request):
    projects=Portafolio.objects.filter(public=True)
    return render(request,'portfolio/portafolio.html',
    {
        'projects': projects
    })