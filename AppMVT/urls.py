from django.urls import path

from AppMVT.views import family

urlpatterns = [
    path('familiar', family),
]
