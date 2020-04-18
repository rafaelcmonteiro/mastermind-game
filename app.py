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
    return render_template('index.html', title='home')


@app.route("/register", methods=['GET', 'POST'])
def register():
    return "Pagina em criação."


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        req = request.form
        login_user = dao.find_user(req.get("username"))

        username = req.get("username")
        password = req.get("password")

        if username != login_user['user'] or login_user is None:
            print("Username not found")
            return redirect(request.url)
        else:
            complete_name = login_user['user']

        if not password == login_user["password"]:
            print("Incorrect password")
            return redirect(request.url)
        else:
            session["USERNAME"] = complete_name
            print(session)
            print("session username set")
            return redirect(url_for("profile"))

    return render_template("login.html", title='login')


@app.route("/profile")
def profile():
    if not session.get("USERNAME") is None:
        username = session.get("USERNAME")
        login_user = dao.find_user(username)
        return render_template("profile.html", user=login_user)
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
    return render_template('mastermind.html', title='game', nav_bar=False)


# This function trigger the game.
@app.route("/mastermind/", methods=['GET', 'POST'])
def mastermind():
    number_typed = request.form['typed-number']
    to_send = l_master.master_mind(number_typed, session['random_number'])
    objectMastermind.list_dict.append(to_send)
    session['list_dict'] = objectMastermind.list_dict
    print(session)
    if len(session['list_dict']) <= 9:
        if to_send['result'] == '1111':
            return render_template('mastermind.html', title='game', tentativas=session['list_dict'], nav_bar=False,
                                   button_disabled=True, success=True, category='success',
                                   message_category='Parabéns, você acertou.'), 200
        else:
            return render_template('mastermind.html', title='game', tentativas=session['list_dict'], nav_bar=False), 200
    else:
        return render_template('mastermind.html', title='game', tentativas=session['list_dict'], nav_bar=False,
                               button_disabled=True, success=True, category='danger',
                               message_category='Você chegou ao limite de tentativas, você perdeu.'), 200


@app.errorhandler(404)
def page_not_found(error):
    return 'A página não existe.', 404


# Código inutil
@app.route("/generate-number/", methods=['GET'])
def random_number():
    str_number = l_master.generate_number()
    return str_number, 200


# This function insert the random number on user dict.
@app.route("/initialize/<string:user_name>/", methods=['GET'])
def to_db(user_name):
    resolution = l_master.inserting_random(user_name)
    return resolution, 200


# Código inutil


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, threaded=True, debug=True)
