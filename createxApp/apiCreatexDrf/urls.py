from django.urls import path


from apiCreatexDrf.views import OurServicesApiView, OurServicesApiViewDetail, NewsModelApiView, NewsModelApiViewDetail, AskFromUserViewAdd, \
    UserSubscribeApiView, DiscussForUserApiView, OurWorkApiView, OurWorkApiViewDetail, OurOfferServicesApiView, OurOfferServicesApiViewDetail

urlpatterns = [
    path('api/servicesList/',OurServicesApiView.as_view()), #Сериализатор - все услуги
    path('api/servicesList/<int:pk>/',OurServicesApiViewDetail.as_view()), #Сериализатор - услуга

    path('api/ourOfferServices/',OurOfferServicesApiView.as_view()),#Сериализатор - оферта список
    path('api/ourOfferServices/<int:pk>/',OurOfferServicesApiViewDetail.as_view()),#Сериализатор - оферта одна запись


    path('api/newsList/',NewsModelApiView.as_view()),#Сериализатор - все новости
    path('api/newsList/<int:pk>',NewsModelApiViewDetail.as_view()),#Сериализатор -новость

    path('api/OurWork/',OurWorkApiView.as_view()),#Сериализатор - все услуги/работы
    path('api/OurWork/<int:pk>',OurWorkApiViewDetail.as_view()),#Сериализатор - услуга/работа

    #Пути для добавления данных
    path('api/askAdd/',AskFromUserViewAdd.as_view()),#Сериализатор - вопрос от пользователя из формы
    path('api/userSubscribeAdd/', UserSubscribeApiView.as_view()),  # Сериализатор - подписчики сайта + подписка на сайт
    path('api/discussForUserAdd/', DiscussForUserApiView.as_view()),  # Сериализатор - Обсуждение от пользователей + форма
]