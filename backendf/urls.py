from django.urls import path
from . import views
from .views import EmailPasswordViewSet

urlpatterns = [
    path('',views.getlog),
    path('service/',views.getservices),
    path('allservices/',views.getallservices),
    path('popular/',views.getpop),
    path('cleaning/',views.cleaning),
    path('insert/',EmailPasswordViewSet.as_view({'post':'insert'}))
]