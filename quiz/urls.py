from django.urls import path, include

from .views import hello_API_hihi, randomQuiz

urlpatterns = [
    path("hello/", hello_API_hihi),
    path("<int:id>/", randomQuiz),
]
