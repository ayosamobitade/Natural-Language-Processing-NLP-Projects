from django.urls import path
from .views import ReviewPageView


urlpatterns = [
    path('review/', ReviewPageView, name='reviewpage')
]