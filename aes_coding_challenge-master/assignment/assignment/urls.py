
from django.contrib import admin
from transaction import views
from django.urls import path
from django.urls.conf import include
from rest_framework import routers



router = routers.DefaultRouter()
router.register("For Trans Doc", views.ViewModel ,basename='Transaction')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('transaction.urls') ),
]
