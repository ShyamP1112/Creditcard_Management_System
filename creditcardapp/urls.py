from django.contrib import admin
from django.urls import path
from creditcardapp import views

urlpatterns = [
   path('admin/',admin.site.urls),
   path('',views.index),
   path('home/',views.home),
   path('about/',views.about),
   path('contact/',views.contact),
   path('creditcardform/',views.creditcardform),
   path('services/',views.services),
   path('client/',views.client),
   path('creditcard/',views.creditcard),


]