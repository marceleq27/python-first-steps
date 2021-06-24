from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Quotes(Resource):
    def get(self):
        return {
            'Elon Musk': {
                'quote': ['Fajnie byłoby umrzeć na Marsie, byle nie rozbić się przy podejściu do lądowania.']
            },
            'Steve Balmer': {
                'quote': ['Mam Maka i czas pracy na bateriach jest fatalny, Mac jest taaaki ciężki. '
                          'Jeśli chcesz długo pracować na komputerze – lepiej zrobić przesiadkę. '
                          'Jeśli chcesz netbooka – lepiej zrobić przesiadkę.'
                          ' Jeśli chcesz korzystać z tych samych aplikacji, które ma Mac plus wielu innych – lepiej zrobić przesiadkę. '
                          'MacBook Air jest lekki? Podnieście te komputery, które mamy tutaj, są dużo lżejsze!']
            },
            'Steve Jobs': {
                'quote': ['Ci, którzy są wystarczająco szaleni, by myśleć, że są w stanie zmienić świat, są tymi, którzy go zmieniają']
            },
            'Bill Gates': {
                'quote':
                ['Obecnie ludzie od bezpieczeństwa włamują się do maców każdego dnia, wymyślają nowe exploity, dzięki którym można całkowicie przejąć kontrolę nad maszyną. Niech ktoś spróbuje coś takiego zrobić z Windowsem chociaż raz na miesiąc.']
            },
            'Janusz': {
                'quote':
                ['Ja chcę powiedzieć jedną rzecz: funkcjonariusze reżymowej telewizji z premedytacją próbują wyrzucić kierowców z miast, bo bez tego (tfu!) demokracja nie może istnieć przez kolejne kadencje. (źródło: https://codepen.io/AubreyDeLosDestinos/details/vwrQxr)']
            },
            'Janusz': {
                'quote':
                ['Trzeba powiedzieć jasno: przedstawiciele czerwonej hołoty celowo i świadomie próbują wyrzucić kierowców z miast, bo dostają za to pieniądze przez kolejne kadencje. (źródło: https://codepen.io/AubreyDeLosDestinos/details/vwrQxr)']
            },
            'Janusz': {
                'quote':
                ['Jak powiedział wybitny krakowianin Stanisław Lem, ci wszyscy (tfu!) demokraci o poglądach na lewo od komunizmu próbują skłócić Polskę z Rosją, bo bez tego (tfu!) demokracja nie może istnieć, o czym się nie mówi. (źródło: https://codepen.io/AubreyDeLosDestinos/details/vwrQxr)']
            }
        }


api.add_resource(Quotes, '/')

if __name__ == '__main__':
    app.run(debug=True)
