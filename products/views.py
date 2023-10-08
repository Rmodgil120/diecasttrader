from django.http import HttpResponse
from django.shortcuts import render
from .models import hotwheels as hw
from .models import maisto as mst
from .models import majorette as mtt
from .models import mathchbox as mb
from .models import tomica as tc


def homepage(request):
    return render(request, 'Home.html')

def hotwheels(request):
    hotwheels_list = hw.objects.all()
    return render(request, 'hotwheels.html', {'hotwheels_list': hotwheels_list})

def maisto(request):
    maisto_list = mst.objects.all()
    return render(request, 'maisto.html', {'maisto_list': maisto_list})

def majorette(request):
    majorette_list = mtt.objects.all()
    return render(request, 'majorette.html', {'majorette_list': majorette_list})

def matchbox(request):
    matchbox_list = mb.objects.all()
    return render(request, 'matchbox.html', {'matchbox_list': matchbox_list})

def tomica(request):
    tomica_list = tc.objects.all()
    return render(request, 'tomica.html', {'tomica_list': tomica_list})

def others(request):
    return render(request, 'others.html')