from flask import Flask, render_template, redirect, url_for, request, session
import mastermind_logic as l_master
import user_dao as dao
from entity.mastermindEntity import DictClass
import bcrypt

app = Flask("mastermind")
app.config['SECRET_KEY'] = '57956B56B56545B'
objectMastermind = DictClass([{}])


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
        if email_from_db is None:
            user_dict = {
                'name': req.get('name'),
                'user': req.get('username'),
                'password': req.get('password')
            }
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
        if login_user is not None:

            if username != login_user['user'] or login_user is None:
                print("Usuario não encontrado.")
                return redirect(request.url)
            else:
                complete_name = login_user['user']

            if not password == login_user["password"]:
                print("Senha Incorreta")
                return redirect(request.url)
            else:
                session["USERNAME"] = complete_name
                print(session)
                print("Session contruida.")
                return redirect(url_for("profile"))
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
        print("No username found in session")
        return redirect(url_for("login"))


@app.route("/log-out")
def sign_out():
    session.clear()
    return redirect(url_for("home"))


@app.route("/game/", methods=['GET'])
def mastermind_game():
    objectMastermind.list_dict.clear()
    session['random_number'] = l_master.generate_number()
    return render_template('mastermind.html', title='Game', nav_bar=True)


# This function trigger the game.
@app.route("/mastermind/", methods=['GET', 'POST'])
def mastermind():
    number_typed = request.form['typed-number']
    to_send = l_master.master_mind(number_typed, session['random_number'])
    # Getting random number from session.
    random_from_session = session['random_number']
    objectMastermind.list_dict.append(to_send)
    session['list_dict'] = objectMastermind.list_dict

    if len(session['list_dict']) <= 9 or to_send['result'] == '1111':
        if to_send['result'] == '1111':
            return render_template('mastermind.html', title='game', tentativas=session['list_dict'], nav_bar=True,
                                   button_disabled=True, success=True, category='success',
                                   message_category='Parabéns, você acertou.',
                                   random_from_session=random_from_session), 200
        else:
            return render_template('mastermind.html', title='Game', tentativas=session['list_dict'], nav_bar=True), 200
    else:
        return render_template('mastermind.html', title='Game', tentativas=session['list_dict'], nav_bar=True,
                               button_disabled=True, success=True, category='danger',
                               message_category='Você chegou ao limite de tentativas, você perdeu.',
                               random_from_session=random_from_session), 200


@app.errorhandler(404)
def page_not_found(error):
    return 'A página não existe.', 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, threaded=True, debug=True)
