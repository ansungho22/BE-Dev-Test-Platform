from rest_framework.views import APIView
from rest_framework.response import Response
from .openweather import weather


class Weather(APIView):
    def get(self, request):
        get_weather = weather
        weather_data = get_weather.return_weather(request.data["city"])
        return Response(weather_data, status=200)
