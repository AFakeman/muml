from api.models import Midi
from rest_framework import serializers


class MidiListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Midi
        fields = ('id', 'name')