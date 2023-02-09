from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('',views.getlog),
    path('service/',views.getservices),
    path('allservices/',views.getallservices),
    path('popular/',views.getpop),
    path('people/',views.people),
    path('insert/',EmailPasswordViewSet.as_view({'post':'insert'})),
    path('peoples/',serviceviewset.as_view({'post':'ins'})),
    path('update/',updateviewset.as_view({'post':'update'}))
]