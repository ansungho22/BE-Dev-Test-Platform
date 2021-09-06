import re
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .openweather import weather
import json


class Weather(APIView):
    def get(self, request):
        get_weather = weather
        weather_data = get_weather.return_weather(request.data["city"])
        return Response(weather_data, status=200)
