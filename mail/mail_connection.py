from flask import Flask
from flask_mail import Mail, Message
import mastermind_logic as l_master

from dao import user_dao as dao

app = Flask("mastermind")


def mail_set():
    with open('game/mail.txt', 'r') as f:
        data = f.readlines()
    email = data[0].strip()
    senha = data[1].strip()

    mail_connection = {
        "MAIL_SERVER": 'smtp.gmail.com',
        "MAIL_PORT": 465,
        "MAIL_USE_TLS": False,
        "MAIL_USE_SSL": True,
        "MAIL_USERNAME": email,
        "MAIL_PASSWORD": senha
    }

    mail_settings = mail_connection
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

