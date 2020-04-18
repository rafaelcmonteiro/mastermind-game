from flask import Flask, render_template, flash, redirect, url_for, request, session
from forms import RegistrationForm, LoginForm
import mastermind_logic as l_master
import user_dao as dao
from entity.mastermindEntity import DictClass
import bcrypt

app = Flask("mastermind")
app.config['SECRET_KEY'] = '57956B56B56545B'
objectMastermind = DictClass([{}])


@app.before_request
def require_login():
    allowed_route = ['login', 'register', 'home', 'mastermind_game', 'mastermind']
    if request.endpoint not in allowed_route:
        return redirect(url_for('login'))


@app.route("/")
@app.route("/home/", methods=['GET'])
def home():
    return render_template('index.html', title='home')


@app.route("/register/", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Encrypting password
        hash_pass = bcrypt.hashpw(form.password.data.encode('utf-8'), bcrypt.gensalt())
        # Making a dictionary
        dict_user = {"name": form.username.data, "user": form.email.data, "password": hash_pass}
        # Creating user
        dao.creating_user(dict_user)
        flash('Account created for {}!'.format(form.username.data), category='success')
        return redirect(url_for('perfil'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login/", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        login_user = dao.find_user(form.email.data)
        if login_user:
            session['email'] = form.email.data
            print(session)
            flash('You have been logged in!', 'success')
            return redirect(url_for('perfil'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='login', form=form)


@app.route("/log-out/")
def sign_out():
    session.clear()
    return redirect(url_for("home"))


# Test
@app.route("/perfil/", methods=['GET'])
def perfil():
    # if 'username' in session:
    # return 'You are logged in as ' + session['username']
    return render_template('perfil.html', title='perfil', nav_bar=True)


@app.route("/generate-number/", methods=['GET'])
def random_number():
    str_number = l_master.generate_number()
    return str_number, 200


# This function insert the random number on user dict.
@app.route("/initialize/<string:user_name>/", methods=['GET'])
def to_db(user_name):
    resolution = l_master.inserting_random(user_name)
    return resolution, 200


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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, threaded=True, debug=True)
