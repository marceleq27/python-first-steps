from flask import Flask
from flask import redirect, url_for, render_template, request
from flask_dance.contrib.github import make_github_blueprint, github
# import flask_login
import secrets
import os
from AzureDB import AzureDB

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)
# login_manager = flask_login.LoginManager()
# login_manager.init_app(app)


os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

github_blueprint = make_github_blueprint(
    client_id="c87d7b00bcb71d06f05c",
    client_secret="2ad0473c07cce169b011981934e961cdcb23e12a",
)
app.register_blueprint(github_blueprint, url_prefix='/login')


@app.route("/")
def home():

    if not github.authorized:
        return redirect(url_for('github.login'))
    else:
        account_info = github.get('/user')
        if account_info.ok:
            account_info_json = account_info.json()
            return render_template("index.html", data=account_info_json['login'])
    return '<h1>Request failed!</h1>'


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


# @app.route("/logout")
# def logout():
#     flask_login.logout_user()
#     return '<h1>You are not authorized!</h1>'


if __name__ == '__main__':
    app.run(debug=True)
