from rest_framework import viewsets, permissions

from .models import Trivia
from .serializers import TriviaSerializer


class TriviaViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TriviaSerializer
    queryset = Trivia.objects.all()
