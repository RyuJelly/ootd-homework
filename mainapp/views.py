from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.template import loader
from mainapp.models import Sido, City, Image
from django.core.paginator import Paginator
from django.templatetags.static import static

# Create your views here.
def main(request) :
    context = {
        'sido_geo': static("sido.geojson"),
        'sigungu_geo': static("sigungu.geojson"),
        'sido_list': Sido.objects.all(),
        'city_list': City.objects.all(),
    }

    return render(request, "main.html", context)
