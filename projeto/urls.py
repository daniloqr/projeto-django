
from django.contrib import admin
<<<<<<< HEAD
from django.urls import include, path
=======
from django.http import HttpResponse
from django.urls import path


def my_view(request):
    return HttpResponse('Hello World')
>>>>>>> f211731afb96136b07890dce3e5a6ce2860bea19


urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('', include('recipes.urls')),
=======
    path('sobre/', my_view),

>>>>>>> f211731afb96136b07890dce3e5a6ce2860bea19
]
