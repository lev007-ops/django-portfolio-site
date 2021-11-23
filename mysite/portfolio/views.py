from django.shortcuts import render
from portfolio.models import Diploma


def home(request):
    diploms = Diploma.objects.all()
    return render(request, 'portfolio/home.html', {'diploms': diploms})
