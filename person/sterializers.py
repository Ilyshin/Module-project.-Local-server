from rest_framework import serializers
from person.models import Person


class PersonDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

class PersonListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'