from flask import Flask
from flask import render_template, request, redirect
from AzureDB import AzureDB

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/aboutme")
def aboutme():
    return render_template("aboutme.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/gallery")
def gallery():
    return render_template("gallery.html")


@app.route("/guests")
def guests():
    with AzureDB() as a:
        data = a.azureGetData()
    return render_template("guests.html", data=data)


@app.route('/add', methods=['POST'])
def add():
    with AzureDB() as a:
        _nick = request.form['exampleInputNick1']
        _text = request.form['exampleInputText1']
        _date = request.form['exampleInputDate1']
        a.cursor.execute(
            "INSERT into data (name, text, date) values (" + "'" + _nick + "'" + "," + "'" + _text + "'" + "," + "'" + _date + "'" + ")")
        a.conn.commit()
    return redirect('/guests')


@app.route('/delete/<string:id>', methods=['POST'])
def delete(id):
    with AzureDB() as a:
        a.cursor.execute(
            "DELETE FROM data WHERE date = " + "'" + id + "'")
        a.conn.commit()
    return redirect('/guests')


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


if __name__ == '__main__':

    app.run(debug=True)
