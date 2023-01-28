from django.urls import path
from . import views
from .views import EmailPasswordViewSet

urlpatterns = [
    path('',views.getlog),
    path('service/',views.getservices),
    path('insert/',EmailPasswordViewSet.as_view({'post':'insert'}))
]