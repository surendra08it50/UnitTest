import requests

def create_weather_subscription(user_id, package_id, start_date, end_date):
    payload = {
        'user_id': user_id,
        'package_id': package_id,
        'start_date': start_date,
        'end_date': end_date,
    }
    response = requests.post(
        'https://dummy-weather-service.com/weather/subscribe/', data=payload
    )
    return response