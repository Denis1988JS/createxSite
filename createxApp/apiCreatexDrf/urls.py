from django.urls import path


from apiCreatexDrf.views import OurServicesApiView, OurServicesApiViewDetail, NewsModelApiView, NewsModelApiViewDetail

urlpatterns = [
    path('api/servicesList/',OurServicesApiView.as_view()), #Сериализатор - все услуги
    path('api/servicesList/<int:pk>/',OurServicesApiViewDetail.as_view()), #Сериализатор - услуга
    path('api/newsList/',NewsModelApiView.as_view()),#Сериализатор - все новости
    path('api/newsList/<int:pk>',NewsModelApiViewDetail.as_view()),#Сериализатор - все новость
]