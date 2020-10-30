from rest_framework import viewsets

from .models import Trivia
from .serializers import TriviaSerializer


class TriviaViewSet(viewsets.ModelViewSet):
    serializer_class = TriviaSerializer
    queryset = Trivia.objects.all()
