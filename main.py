import requests
from secerts import API_KEY


def get_current_temperature(city):
    url = (f'http://api.weatherapi.com/v1/forecast.json?key={API_KEY} &q={city}'
           f'&days=1&aqi=no&alerts=no')
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        print(f"{city} Current Temperature in celsius", data['current']['temp_c'])
        return response.text
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)
        return None


def get_lat_long(city):
    url = (f'http://api.weatherapi.com/v1/forecast.json?key={API_KEY} &q={city}'
           f'&days=1&aqi=no&alerts=no')
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        print(f"{city} Lat: ", data['location']['lat'])
        print(f"{city} Long: ", data['location']['lon'])
        return response.text
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)
        return None


def get_temperature_after(city, days, hour='none'):
    url = (f'http://api.weatherapi.com/v1/forecast.json?key={API_KEY} &q={city}'
           f'&days={days}&hour={hour}&aqi=no&alerts=no')
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        print_temp_days(data, days, hour)
        return response.text
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)
        return None


def print_temp_days(data, days, hour='none'):
    for i in range(days):
        print(f"\nfor day {i + 1} the temperature as follows")
        if hour != 'none':
            print("Temperature in celsius", data['forecast']['forecastday'][i]['hour'][0]['temp_c'],
                  f"at {hour} as 24-hour format")
        else:
            for j in range(24):
                print("Temperature in celsius", data['forecast']['forecastday'][i]['hour'][j]['temp_c'],
                      f"at {j} as 24-hour format")


if __name__ == "__main__":
    input_city = input("please enter the city you want to get its data: ")
    input_days = input("for how many days (1 for today): ")
    input_hours = input("which hour you want to get its temperature (write none for all the day): ")

    if input_days.isnumeric():
        if input_city.isalpha() and (input_hours.lower() == 'none' or input_hours.isnumeric()):
            fetched_data = get_current_temperature(input_city)
            fetched_lat_long = get_lat_long(input_city)
            fetched_temperature_after = get_temperature_after(input_city, int(input_days), input_hours)
        else:
            print('Please make sure you got all data correctly ')
    else:
        print("please enter days in correct format")
