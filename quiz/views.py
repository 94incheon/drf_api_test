from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Quiz
from .serializers import QuizSerializer

import random

# Create your views here.
@api_view(['GET'])
def hello_API_hihi(reqeust):
    return Response('hello world')

@api_view(['GET'])
def randomQuiz(request, id): # 주어진 개수만큼 랜덤한 퀴즈를 반환하는 API
    totalQuizs = Quiz.objects.all()
    randomQuizs = random.sample(list(totalQuizs), id)
    serializers = QuizSerializer(randomQuizs, many=True) # randomQuize 쿼리셋이 여러개일때 many=True
    return Response(serializers.data)

