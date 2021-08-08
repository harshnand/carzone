from django.shortcuts import render
from .models import Team
from cars.models import Car

# Create your views here.
def home(request):
    team=Team.objects.all()
    featured_car=Car.objects.order_by('-created_date').filter(is_featured=True)
    all_car=Car.objects.all().order_by('-created_date')
    # search_field=Car.objects.values('model','city','year','body_style')
    model_field=Car.objects.values_list('model',flat=True).distinct()
    city_field = Car.objects.values_list('city', flat=True).distinct()
    year_field = Car.objects.values_list( 'year', flat=True).distinct()
    body_field = Car.objects.values_list( 'body_style', flat=True).distinct()
    return render(request,"home.html",{
        "teams":team,
        "featured_car":featured_car,
        "all_car":all_car,
        "body_field":body_field,
        "year_field":year_field,
        "city_field":city_field,
        "model_field":model_field,
    })





def about(request):
    team = Team.objects.all()
    return render(request,"about.html",{
        "teams": team
    })


def services(request):
    return render(request,"services.html")


def contact(request):
    return render(request,"contact.html")