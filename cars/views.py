from django.shortcuts import render,get_object_or_404
from .models import Car
# Create your views here.
def cars(request):
    cars=Car.objects.all()

    return render(request,"cars.html",{
        "cars":cars,

    })

def car_detail(request,id):
    # single_car =get_object_or_404(Car,pk=id)
    single_car= Car.objects.get(pk=id)
    return render(request,"car_detail.html",{
        "single_car":single_car,

    })

def search(request):
    cars=Car.objects.order_by('-created_date')
    if 'keyword' in request.GET:
        keyword=request.GET['keyword']
        if keyword:
            cars=cars.filter(description__icontains=keyword)
    if 'model' in request.GET:
        model = request.GET['model']
        if model:
            cars = cars.filter(model__iexact=model)
    if 'city' in request.GET:
        city=request.GET['city']
        if city:
            cars=cars.filter(city__iexact=city)

    if 'year' in request.GET:
        year = request.GET['year']
        if year:
            cars = cars.filter(year__iexact=year)

    if 'body_style' in request.GET:
        body_style= request.GET['body_style']
        if body_style:
            cars = cars.filter(body_style__iexact=body_style)

    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price:
            cars=cars.filter(price__gt=min_price,price__lt=max_price)

    return render(request,"search.html",{
       "car":cars
    })
