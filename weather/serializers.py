from rest_framework import serializers
from weather.models import Weather


class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = '__all__'
        #fields = ('id', 'song', 'singer', 'last_modify_date', 'created')