from django.urls import path, include
from .views import CategoryAPIView, VideoAPIView, TourAPIView, HotelAPIView
urlpatterns = [
    path('category/', CategoryAPIView.as_view()),
    path('category/<int:pk>/', CategoryAPIView.as_view()),
    path('video/', VideoAPIView.as_view()),
    path('video/<int:pk>/', VideoAPIView.as_view()),
    path('tour/', TourAPIView.as_view()),
    path('tour/<int:pk>/', TourAPIView.as_view()),
    path('hotel/', HotelAPIView.as_view()),
    path('hotel/<int:pk>/', HotelAPIView.as_view()),

]