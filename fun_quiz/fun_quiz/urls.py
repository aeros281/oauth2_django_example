from django.urls import path, include

from rest_framework import routers

from trivia import views

router = routers.DefaultRouter()
router.register(r'trivia', views.TriviaViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
