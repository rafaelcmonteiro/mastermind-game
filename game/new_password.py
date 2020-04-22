import bcrypt
from flask import render_template, request, session, Flask, url_for
from flask import Blueprint
from flask_mail import Mail, Message
from werkzeug.utils import redirect
import user_dao as dao
import mastermind_logic as l_master
from entity.mastermindEntity import DictClass

# Templates : new_password.html, sending_token.html, token.html
app = Flask("mastermind")

mastermind_game_bp_2 = Blueprint('new_password', 'mastermind')


def mail_set():
    with open('texto.txt', 'r') as f:
        valor = f.read()
    mail_settings = valor
    app.config.update(mail_settings)
    mail = Mail(app)
    return mail


def sending_email(mail_user):
    mail_token = l_master.generate_number()
    token_dict = {"token": mail_token}
    dao.updating_user(mail_user, token_dict)
    mail = mail_set()
    with app.app_context():
        msg = Message(subject="Hello",
                      sender=app.config.get("MAIL_USERNAME"),
                      recipients=[mail_user],
                      body="Seu token é {}".format(mail_token))
        mail.send(msg)


@mastermind_game_bp_2.route('/sending-token', methods=['GET', 'POST'])
def sending_token():
    if request.method == 'POST':
        req = request.form
        email = req.get('username')
        user_data = dao.find_user(email)
        if user_data is not None:
            # Fazer a verificação no banco para poder enviar um e-mail
            session['email'] = email
            print(session)
            sending_email(email)
            return redirect(url_for("new_password.confirm_token"))
    return render_template('sending_token.html')


@mastermind_game_bp_2.route('/confirm-token', methods=['GET', 'POST'])
def confirm_token():
    if request.method == 'POST':
        if not session.get("email") is None:
            email = session['email']
            user_data = dao.find_user(email)
            mail_token = user_data['token']
            if user_data is not None:
                # Fazer outra verificação no banco.
                req_token = request.form
                token_from_email = req_token.get('token')
                if mail_token == token_from_email:
                    return redirect(url_for("new_password.new_password"))
    return render_template('token.html')


@mastermind_game_bp_2.route('/new-password', methods=['GET', 'POST'])
def new_password():
    if request.method == 'POST':
        email = session['email']
        req = request.form
        password = req.get('password')
        encoded_password = password.encode('utf-8')
        hashed = bcrypt.hashpw(encoded_password, bcrypt.gensalt())
        password_dict = {
            'password': hashed
        }
        dao.updating_user(email, password_dict)
        return render_template('login.html')
    return render_template('new_password.html')
