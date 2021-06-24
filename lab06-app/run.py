from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def home():

    if request.method == 'GET':
        return render_template('home.html')
    if request.method == 'POST':
        artist = request.form['artist']
        info = requests.get('http://localhost:5000/' + artist)
        print(info)
        data = info.json()
        return render_template('home.html', data=data)
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
