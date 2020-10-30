from rest_framework import serializers

from .models import Trivia


class TriviaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Trivia
        fields = ['short_description', 'long_description']
