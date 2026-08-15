from django.urls import path
from .views import HealthCheckAPIView
from .views.upload_views import PresignedUrlView

urlpatterns = [
    path("health/", HealthCheckAPIView.as_view()),
    path("upload/presigned-url/", PresignedUrlView.as_view(), name="presigned-url"),
]