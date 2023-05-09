import requests
import sys


line_of_cities = []
for city in sys.stdin:
    line_of_cities.append(city)
the_southest_city = ''
answer = 90
for city in line_of_cities:
    geocoder_request = f"http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode={city}&format=json"
    response = requests.get(geocoder_request)
    if response:
        json_response = response.json()
        latitude = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"].split()
        if float(latitude[1]) < answer:
            answer = float(latitude[1])
            the_southest_city = city
    else:
        print("Ошибка выполнения запроса:")
print(the_southest_city)
