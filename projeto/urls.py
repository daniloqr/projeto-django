
""" from django.urls import path """
from django.http import HttpResponse
from django.urls import include, path
from django.contrib import admin


def my_view(request):
    return HttpResponse('Hello World')


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('recipes.urls')),


]
