from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('',views.getlog),
    path('service/',views.getservices),
    path('allservices/',views.getallservices),
    path('popular/',views.getpop),
    path('people/',views.people),
    path('review/',views.review),
    #path('star/',views.getstar),
    path('insert/',EmailPasswordViewSet.as_view({'post':'insert'})),
    path('peoples/',serviceviewset.as_view({'post':'ins'})),
    path('update/',updateviewset.as_view({'post':'update'})),
    path('delete/',deleteviewset.as_view({'post':'delete'})),
    path('updatestar/',updatestar.as_view({'post':'updaterate'})),
    path('send/',reviewserviceset.as_view({'post':'place'}))
]