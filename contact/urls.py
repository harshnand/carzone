from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
         path('inquiry',views.inquiry, name="inquiry")
    # path('inquiry', views.inquiry.as_view(), name="inquiry")

]
