from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Mata(Resource):
    def get(self):
        return {
            'songs': [{
                'title': 'Patoreakcja',
                'album': 'Patoreakcja',
                'time': '3:42',
                'type': 'mp3',
                'artist': 'Mata',
            }]}


class Ekipa(Resource):
    def get(self):
        return {
            'songs': [{
                'title': '3KIPA',
                'album': '3KIPA',
                'time': '3:22',
                'type': 'mp3',
                'artist': 'Ekipa'
            }]}


class Kizo(Resource):
    def get(self):
        return {
            'songs': [{
                'title': 'Espresso',
                'artist': 'Kizo',
                'album': 'Posejdon',
                'time': '2:55',
                'type': 'mp3'}]
        }


class Pezet(Resource):
    def get(self):
        return {
            'songs': [{
                'title': 'Magenta',
                'artist': 'Pezet',
                'album': 'Muzyka współczesna',
                'time': '5:11',
                'type': 'mp4'
            }]}


api.add_resource(Mata, '/mata')
api.add_resource(Ekipa, '/ekipa')
api.add_resource(Kizo, '/kizo')
api.add_resource(Pezet, '/pezet')

if __name__ == '__main__':
    app.run(debug=True)
