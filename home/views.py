from django.shortcuts import render
from .models import Project
# Create your views here.

def index(request):
    pro = Project.objects.all()
    return render(request, 'index.html', {'pro': pro})
