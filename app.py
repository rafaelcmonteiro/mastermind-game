from flask import Flask, render_template, flash, redirect, url_for, request, session
from forms import RegistrationForm, LoginForm
import mastermind_logic as l_master
import user_dao as dao
import bcrypt
import mastermind_entity as entity

app = Flask("mastermind")
app.config['SECRET_KEY'] = '57956B56B56545B'
list_dict = []

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
        session['username'] = form.email.data
        flash('Account created for {}!'.format(form.username.data), category='success')
        return redirect(url_for('perfil'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login/", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        login_user = dao.find_user(form.email.data)
        if login_user:
            flash('You have been logged in!', 'success')
            return redirect(url_for('perfil'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='login', form=form)


# Test
@app.route("/perfil/", methods=['GET'])
def perfil():
    if 'username' in session:
        return 'You are logged in as ' + session['username']
    return render_template('perfil.html', titulo='login')


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
    return render_template('mastermind.html', titulo='game')


# This function trigger the game.
@app.route("/mastermind/", methods=['GET', 'POST'])
def mastermind():
    number_typed = request.form['typed-number']
    to_send = l_master.master_mind(number_typed)
    list_dict.append(to_send)
    return render_template('mastermind.html', titulo='game', tentativas=list_dict), 200


@app.errorhandler(404)
def page_not_found(error):
    return 'A página não existe.', 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, threaded=True, debug=True)
