import requests
import json


class weather:
    def return_weather(name):

        k2c = lambda k: k - 273.15
        url = (
            "http://api.openweathermap.org/data/2.5/weather?q=%s&appid=dc070279954507e9bc552aa7c1e85e80"
            % name
        )
        r = requests.get(url)
        data = r.json()
        weather_json = {
            "도시": data["name"],
            "날씨": data["weather"][0]["description"],
            "최저 기온": k2c(data["main"]["temp_min"]),
            "최고 기온": k2c(data["main"]["temp_max"]),
            "습도": data["main"]["humidity"],
            "기압": data["main"]["pressure"],
            "풍향": data["wind"]["deg"],
            "풍속": data["wind"]["speed"],
        }
        prov_list = [
            {"name": "Seoul", "city_id": "1835847"},
            {"name": "Busan", "city_id": "1838524"},
            {"name": "Daegu", "city_id": "1835329"},
            {"name": "Incheon", "city_id": "1843564"},
            {"name": "Gwangju", "city_id": "1841811"},
            {"name": "Daejeon", "city_id": "1835235"},
            {"name": "Ulsan", "city_id": "1833747"},
            {"name": "Sejong", "city_id": "1835235"},
            {"name": "Gyeonggi", "city_id": "1841610"},
            {"name": "Gangwon", "city_id": "1843125"},
            {"name": "Chungcheongbuk", "city_id": "1845106"},
            {"name": "Chungcheongnam", "city_id": "1845105"},
            {"name": "Jeollabuk", "city_id": "1845789"},
            {"name": "Jeollanam", "city_id": "1845788"},
            {"name": "Gyeongsangbuk", "city_id": "1841597"},
            {"name": "Gyeongsangnam  ", "city_id": "1902028"},
            {"name": "Jeju", "city_id": "1846266"},
        ]
        return weather_json
