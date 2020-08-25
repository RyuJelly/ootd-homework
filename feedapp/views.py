from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.template import loader
from mainapp.models import Sido, City, Image
from django.core.paginator import Paginator
from django.templatetags.static import static
from datetime import date


# Create your views here.
def feed(request):
    city = int(request.GET['city'][:5])
    today = date.today()

    # 지역 걸러내기(image.city) + 오늘날짜
    if request.method == "POST":
        sort = request.POST.get("sort")
        if sort != "":
            olist = Image.objects.filter(city_id=city,
                                         image_date__month=today.month,
                                         image_date__day=today.day).order_by(sort).reverse()
    else:
        # 실시간 (기본)
        olist = Image.objects.filter(city_id=city,
                                     image_date__month=today.month,
                                     image_date__day=today.day).order_by('image_date').reverse()

    # 인기순
    # olist = Image.objects.filter(city_id=city,
    #                              image_date__month=today.month,
    #                              image_date__day=today.day).order_by('image_like').reverse()

    # 조회순
    # olist = Image.objects.filter(city_id=city,
    #                              image_date__month=today.month,
    #                              image_date__day=today.day).order_by('image_cnt').reverse()

    # 과거 피드 더 보기

    context = {"olist": olist}
    return render(request, 'feed.html', context)