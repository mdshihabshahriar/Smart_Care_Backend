from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .import views

router = DefaultRouter()  # amader router

router.register('',views.ContactUsViewset)  # router er antena

urlpatterns = [
    path('',include(router.urls)),
]
