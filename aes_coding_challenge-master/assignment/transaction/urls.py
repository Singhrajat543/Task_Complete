from django.urls import path
from transaction import views



urlpatterns=[
path('',views.ApiOverview),
path('ViewModel/',views.ViewModel),
path('AddTrancDoc/',views.AddTrancDoc, name="AddTrancDoc"),
path('AddLineItem/',views.AddLineItem, name="AddLineItem"),
path('AddInventryToLineItem/',views.AddInventryToLineItem, name="AddInventryToLineItem"),
path('deleteMethod/<str:pk>/',views.deleteMethod, name="deleteMethod"),








    
]