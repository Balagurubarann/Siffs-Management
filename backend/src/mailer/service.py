from flask_mail import Message
from flask import render_template, current_app
from src.extension import mail
from threading import Thread

def _send_async(app, msg):

    with app.app_context():

        mail.send(msg)

def send_welcome_mail(to_email, username, password, role):

    msg = Message(
        subject="Joining Confirmation - SIFFS",
        recipients=[to_email]
    )

    msg.html = render_template(
        "email/welcome.html",
        username=username,
        password=password,
        role=role
    )

    Thread(
        target=_send_async,
        args=(current_app._get_current_object(), msg)
    ).start()
