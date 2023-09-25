from django.shortcuts import render
from .models import Finch

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finchs_index(request):
  return render(request, 'finchs/index.html', {
    'finchs': finchs
  })


def finchs_detail(request, finchs_id):
  cat = Finch.objects.get(id=finch_id)
  return render(request, 'finchs/detail.html', {'finch': cat})


def all_finches(request):
    finches = Finch.objects.all()
    return render(request, 'all.html', {'finches': finches})
