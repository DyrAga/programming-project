import requests
import geocoder
from flask import Flask, request, render_template
import plots
import time

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/show_weather', methods = ['POST'])
def show_weather():
    inserted_location = request.form['location']
    location = geocoder.osm(inserted_location, ssl_verify = False)
    latitude, longitude = location.latlng
    latitude = round(latitude, 2)
    longitude = round(longitude, 2)
    params = {
        'latitude': latitude,
        'longitude': longitude,
        'past_days': 7,
        'hourly': 'temperature_2m,cloud_cover,precipitation'
    }
    response = requests.get('https://api.open-meteo.com/v1/forecast', params = params)
    if response.status_code == 200:
        data = response.json()
        data = data['hourly']
        date = data['time']
        temperature = data['temperature_2m']
        cloud_cover = data['cloud_cover']
        precipitation = data['precipitation']
        plots.draw_temperature_plot(date, temperature)
        plots.draw_cloud_cover_plot(date, cloud_cover)
        plots.draw_precipitation_plot(date, precipitation)
        cache_buster = int(time.time())
        return render_template('weather.html', location = inserted_location,
                                temperature_plot = 'temperature_plot.png',
                                cloud_cover_plot = 'cloud_cover_plot.png',
                                precipitation_plot = 'precipitation_plot.png',
                                cache_buster = cache_buster)
    else:
        error_message = f'Error: {response.status_code}, {response.text}'
        return render_template('error.html', error_message = error_message)

if __name__ == '__main__':
    app.debug = True
    app.run()