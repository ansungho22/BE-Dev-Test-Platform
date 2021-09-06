from django.urls import path, include
from .views import *

urlpatterns = [
    path("post/", PostAPIView.as_view()),
    path("post/<int:pk>/", PostAPIView.as_view()),
    path("imgupload/", ImageAPIView.as_view()),
]
