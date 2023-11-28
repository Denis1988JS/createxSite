Web - приложение - сайт строительной компании - createx

В проекте реализован весь функционал по макету , но по причине отсутствия необходимых медиафайлов - некоторые страницы будут
либо пустые либо без функционала

Так же - сайт не адаптирован под мобильные устройства и десктопы ниже 1230 px.

В процессе создания внесены изменения которые не отображены в таблицах и схемах проекта...

В проекте реализован DRF - через модели

На данный момент - проект завершен, в скором времени будут исправлены незначительные ошибки - AJAX запрос (он работает но вве же)
и синтаксическая ошибка в слайдере 



Админка - root - Qwerty
База на sqlLite.
1. Список приложений проекта - homepage
   ['createx +','services +','work +','aboutUs','news','contacts']

-Приложение createx- главная страница:
	модели: mainSlider +, ourCoreValues +, ourServices +, ourWork,ourPartners +,clientsReviews+,ourNews,
	формы: questionsForUser+ ,discussForUser+ ,userSubscribe+

-Приложение services - услуги компании (все services-list)- homepage/services
	модели: ourServices+
	формы: discussForUser+,userSubscribe+

страница services/ - СТРАНИЦА ГОТОВА
	перечень услуг +, навигация+, форма обсуждения+, футер сайта + .
 
страница services/services_slug (services detail) - 
	модели: ourServices_slug+,ourOfferServices+,ourBenefits+,ourWork,ourPartners+
	формы: discussForUser+,userSubscribe+

-Приложение work (все work-list) - выполненные работы -homepage/work Страница готова
	модели: ourServices+, ourWork+, clientsReviews+
	формы: discussForUser+,userSubscribe+ Добавить AJAX - загрузку

страница homepage/work - фильтрация по виду проекта СТРАНИЦА ГОТОВА
	

страница homepage/ work/work_slug (work detail) СТРАНИЦА ГОТОВА
	модели: ourWork+, ourWorkPhotoSliders+, ourWorkPhotoData+, 
	формы: discussForUser+,userSubscribe+

-Приложение AboutUs - услуги компании (все services-list)- homepage/about_us СТРАНИЦА ГОТОВА
	модели: ourCoreValues+, ourHistory+,  ourEmployee+
	формы: discussForUser+,userSubscribe+

страница   homepage/about_us/avaliable_positions (Вакансии)
	модели: avaliablePositions+, employeeBenefits+
	формы: cvFromUser+, subscriberNewVacansies+,discussForUser+,userSubscribe+

-Приложение news  - новости компании (все news-list) - - homepage/news
	модели: ourNews, ourNewsTheme
	формы: discussForUser,userSubscribe
страница homepage/news /news_slug
	модели: news, newCommentsUser
	формы: newsCommentUser,discussForUser,userSubscribe

-Приложение Contacts - контакты компании -  homepage/contacts
	модели: ourOffices, ourSocLinks ,contactUs
	формы: contactUs,userSubscribe






