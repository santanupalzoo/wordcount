
# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.homepages, name ='home'),
    path('count/', views.count, name='count'),
    path('about/', views.about, name='about'),
]
