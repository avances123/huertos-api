from rest_framework import serializers
from actstream.models import Action
from django.contrib.auth.models import User
from farms.models import Farm
from farms.serializers import FarmSerializer


class ActorField(serializers.RelatedField):

    def to_representation(self, value):
        if isinstance(value, User):
            return value.username
        raise Exception('Unexpected type of actor object')

class TargetField(serializers.RelatedField):

    def to_representation(self, value):
        return "kakoasdfas"

class ActionObjectField(serializers.RelatedField):

    def to_representation(self, value):
        if isinstance(value, Farm):
            serializer = FarmSerializer(value)
            return serializer.data
        raise Exception('Unexpected type of actor object')


class ActionSerializer(serializers.ModelSerializer):
    actor = ActorField(read_only=True)
    target = TargetField(read_only=True)
    action_object = ActionObjectField(read_only=True)

    class Meta:
        model = Action
        fields = ['id','actor','verb','action_object','target','timestamp']