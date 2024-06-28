import requests
import csv
from datetime import datetime, timedelta

# Function to fetch weather data from the API for a specific date range
def fetch_weather_data(api_key, location, start_date, end_date):
    url = f"http://api.worldweatheronline.com/premium/v1/past-weather.ashx?key={api_key}&q={location}&format=json&date={start_date}&enddate={end_date}"
    response = requests.get(url)
    try:
        data = response.json()
    except requests.exceptions.JSONDecodeError as e:
        print(f"Error decoding JSON for date range {start_date} to {end_date}: {e}")
        print(f"Response text: {response.text}")
        return None
    return data

# Function to convert weather data to CSV
def weather_data_to_csv(api_key, location, start_date, end_date, csv_file_path):
    with open(csv_file_path, 'w', newline='') as csvfile:
        fieldnames = [
            'date', 'time', 'maxtempC', 'mintempC', 'totalSnow_cm', 'sunHour', 
            'uvIndex', 'moon_illumination', 'moonrise', 'moonset', 'sunrise', 'sunset',
            'DewPointC', 'FeelsLikeC', 'HeatIndexC', 'WindChillC', 'WindGustKmph', 
            'cloudcover', 'humidity', 'precipMM', 'pressure', 'tempC', 'visibility', 
            'winddirDegree', 'windspeedKmph'
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        current_start_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date_dt = datetime.strptime(end_date, '%Y-%m-%d')

        while current_start_date <= end_date_dt:
            current_end_date = current_start_date + timedelta(days=30)
            if current_end_date > end_date_dt:
                current_end_date = end_date_dt
            
            data = fetch_weather_data(api_key, location, current_start_date.strftime('%Y-%m-%d'), current_end_date.strftime('%Y-%m-%d'))
            if data is None:
                current_start_date = current_end_date + timedelta(days=1)
                continue

            for weather in data['data']['weather']:
                date = weather['date']
                astronomy = weather['astronomy'][0]
                for hourly in weather['hourly']:
                    row = {
                        'date': date,
                        'time': hourly['time'],
                        'maxtempC': weather['maxtempC'],
                        'mintempC': weather['mintempC'],
                        'totalSnow_cm': weather['totalSnow_cm'],
                        'sunHour': weather['sunHour'],
                        'uvIndex': weather['uvIndex'],
                        'moon_illumination': astronomy['moon_illumination'],
                        'moonrise': astronomy['moonrise'],
                        'moonset': astronomy['moonset'],
                        'sunrise': astronomy['sunrise'],
                        'sunset': astronomy['sunset'],
                        'DewPointC': hourly['DewPointC'],
                        'FeelsLikeC': hourly['FeelsLikeC'],
                        'HeatIndexC': hourly['HeatIndexC'],
                        'WindChillC': hourly['WindChillC'],
                        'WindGustKmph': hourly['WindGustKmph'],
                        'cloudcover': hourly['cloudcover'],
                        'humidity': hourly['humidity'],
                        'precipMM': hourly['precipMM'],
                        'pressure': hourly['pressure'],
                        'tempC': hourly['tempC'],
                        'visibility': hourly['visibility'],
                        'winddirDegree': hourly['winddirDegree'],
                        'windspeedKmph': hourly['windspeedKmph']
                    }
                    writer.writerow(row)

            current_start_date = current_end_date + timedelta(days=1)

# Replace with your API key, location, start date, and end date
api_key = 'f16238a171494510b8f113758242706'
location = 'Addis Ababa'
start_date = '2014-01-01'
end_date = '2024-01-01'

# Write weather data to CSV
csv_file_path = 'addis_ababa_weather_data.csv'
weather_data_to_csv(api_key, location, start_date, end_date, csv_file_path)

print(f"Weather data has been written to {csv_file_path}")
