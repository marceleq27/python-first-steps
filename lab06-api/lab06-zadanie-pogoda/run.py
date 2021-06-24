from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def home():

    if request.method == 'GET':
        return render_template('home.html')
    if request.method == 'POST':
        city = request.form['city']
        weather_data = format_response(city)
        return render_template('home.html', data=weather_data)
    return render_template('home.html')


def format_response(city):
    weather_key = "fd0c7244de93ccf1ff991b24b2358a5a"
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"APPID": weather_key, "q": city, "units": "Metric"}
    response = requests.get(url, params=params)
    weather = response.json()
    name = weather['name']
    desc = weather['weather'][0]['description']
    temp = weather['main']['temp']
    hum = weather['main']['humidity']
    wind = weather['wind']['speed']
    clouds = weather['clouds']['all']
    pressure = weather['main']['pressure']

    return "City %s Condition: %s Temperature : %s (C) Humadity : %s word Wind speed: %s Cloudness: %s Pressure: %s" % (
        name, desc, temp, hum, wind, clouds, pressure)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
