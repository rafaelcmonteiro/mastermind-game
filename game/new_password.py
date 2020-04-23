import bcrypt
from flask import render_template, request, session, Flask, url_for
from flask import Blueprint
from werkzeug.utils import redirect
from dao import user_dao as dao
from mail.mail_connection import sending_email

# Templates : new_password.html, sending_token.html, token.html
app = Flask("mastermind")

mastermind_game_bp_2 = Blueprint('new_password', 'mastermind')


@mastermind_game_bp_2.route('/sending-token', methods=['GET', 'POST'])
def sending_token():
    if request.method == 'POST':
        req = request.form
        email = req.get('username')
        user_data = dao.find_user(email)
        if user_data is not None:
            # Fazer a verificação no banco para poder enviar um e-mail
            session['email'] = email
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
    return render_template('token.html', success=True, category="success",
                           message_category='Confirme o token enviado para o e-mail')


@mastermind_game_bp_2.route('/new-password', methods=['GET', 'POST'])
def new_password():
    if request.method == 'POST':
        if not session.get("email") is None:
            email = session['email']
            req = request.form
            password = req.get('password')
            encoded_password = password.encode('utf-8')
            hashed = bcrypt.hashpw(encoded_password, bcrypt.gensalt())
            password_dict = {
                'password': hashed
            }
            dao.updating_user(email, password_dict)
            return render_template('login.html', success=True, category="success",
                                   message_category='Senha Alterada.', nav_bar=True)
    return render_template('new_password.html', success=True, category="success",
                           message_category='Token Confirmado.')
