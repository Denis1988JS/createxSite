from django.urls import path

from apiCreatexDrf.views import OurServicesApiView, OurServicesApiViewDetail

urlpatterns = [
    path('api/servicesList/',OurServicesApiView.as_view()),
    path('api/servicesList/<int:pk>/',OurServicesApiViewDetail.as_view()),
]