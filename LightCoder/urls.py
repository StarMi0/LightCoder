from django.contrib import admin
from django.urls import path
from LightCoder import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # main urls
    path('', views.main, name='main'),
    path('about_us/', views.about_us, name='about_us'),
    path('contacts/', views.contacts, name='contacts'),

]
