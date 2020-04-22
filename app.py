from flask import Flask, render_template, redirect, url_for, request, session
from game.mastermind_game import mastermind_game_bp
from game.new_password import mastermind_game_bp_2

import user_dao as dao
from entity.userEntity import User
import bcrypt

app = Flask("mastermind")
app.register_blueprint(mastermind_game_bp)
app.register_blueprint(mastermind_game_bp_2)
app.config['SECRET_KEY'] = '57956B56B56545B'


@app.route("/")
@app.route("/home/", methods=['GET'])
def home():
    return render_template('index.html', title='Home')


@app.route("/register/", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        req = request.form
        email = req.get('username')
        email_from_db = dao.find_user(email)

        password = req.get('password')
        encoded_password = password.encode('utf-8')
        hashed = bcrypt.hashpw(encoded_password, bcrypt.gensalt())
        if email_from_db is None:
            user_dict = User(req.get('name'), req.get('username'), hashed).turn_into_dict()
            id_user = dao.creating_user(user_dict)
            return render_template("login.html", title='login', success=True, category="success",
                                   message_category="Cadastro realizado com sucesso!!")
        else:
            return render_template("register.html", title='registro', success=True, category="danger",
                                   message_category='E-mail já cadastrado na base de dados. Tente outro.')
    else:
        return render_template('register.html', title='Cadastro')


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        req = request.form
        login_user = dao.find_user(req.get("username"))

        username = req.get("username")
        password = req.get("password")
        password = password.encode('utf-8')
        if login_user is not None:
            if username != login_user['user']:
                print("Usuario não encontrado.")
                return redirect(request.url)
            else:
                complete_name = login_user['user']

            if bcrypt.checkpw(password, login_user["password"]):
                session["USERNAME"] = complete_name
                print(session)
                print("Session contruida.")
                return redirect(url_for("profile"))
            else:
                print("Senha Incorreta")
                return redirect(request.url)
        else:
            return render_template("login.html", title='login', success=True, category="danger",
                                   message_category='Usuário ou senha inválidos.')
    return render_template("login.html", title='Login')


@app.route("/profile")
def profile():
    if not session.get("USERNAME") is None:
        username = session.get("USERNAME")
        login_user = dao.find_user(username)
        return render_template("profile.html", user=login_user, nav_bar=True)
    else:
        print("Nenhum usuário encontrado na session.")
        return redirect(url_for("login"))


@app.route("/log-out")
def sign_out():
    session.clear()
    return redirect(url_for("home"))


@app.errorhandler(404)
def page_not_found(error):
    return render_template("error.html"), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, threaded=True, debug=True)
