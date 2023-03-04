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
    path('contact/',views.contact),
    path('homeimage/',views.getimg),
    path('previousstar/',views.previousreview),
    #path('star/',views.getstar),
    path('insert/',EmailPasswordViewSet.as_view({'post':'insert'})),
    path('peoples/',serviceviewset.as_view({'post':'ins'})),
    path('update/',updateviewset.as_view({'post':'update'})),
    path('delete/',deleteviewset.as_view({'post':'delete'})),
    path('updatestar/',updatestar.as_view({'post':'updaterate'})),
    path('send/',reviewserviceset.as_view({'post':'place'})),
    path('updatesend/',updatereviewserviceset.as_view({'post':'updateplace'})),
    path('contactupdate/',contactviewset.as_view({'post':'contactset'})),
    path('updatereview/',updatereviewset.as_view({'post':'updatereview'})),
    path('insertprevious/',insertpreviousstar.as_view({'post':'insertprevious'})),
    path('updateprevious/',updatepreviousstar.as_view({'post':'updateprevious'}))

]