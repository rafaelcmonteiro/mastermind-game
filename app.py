from flask import Flask, render_template, flash, redirect, url_for
from forms import RegistrationForm, LoginForm
import mastermind_logic as l_master

app = Flask("mastermind")
app.config['SECRET_KEY'] = '57956B56B56545B'


@app.route("/")
@app.route("/home/", methods=['GET'])
def home():
    return render_template('index.html', title='home')


@app.route("/register/", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash('Account created for {}!'.format(form.username.data), category='success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login/", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='login', form=form)


# Test
@app.route("/perfil/", methods=['GET'])
def perfil():
    dict_user = {"name": "Rafael", "best_time": "5"}
    return render_template('perfil.html', titulo='login', usuario=dict_user)


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
@app.route("/mastermind/<string:number_typed>/<string:user>/", methods=['GET'])
def mastermind(number_typed, user):
    to_send = l_master.master_mind(number_typed, user)
    return to_send, 200


@app.errorhandler(404)
def page_not_found(error):
    return 'A página não existe.', 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, threaded=True, debug=True)
