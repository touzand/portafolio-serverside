from flask import Flask, send_from_directory, url_for, request
from flask_cors import CORS
from flask_mail import Message, Mail
from dotenv import load_dotenv
import os

app = Flask(__name__)
CORS(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_SECRET_KEY')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_USERNAME')

mail = Mail(app)

@app.route("/")
def hello():
    return "<p>yes ... it works</p>"

@app.route("/articles")
def articles():
    return send_from_directory("static","articles.json")

@app.route("/send_email",methods=['POST'])
def send_email():
    name = request.form['name']
    subject = request.form['subject']
    email = request.form['email']

    msg = Message(subject,
      sender=email,
      recipients=[ os.getenv("MAIL_USERNAME") ])

    msg.html = f"""<div>
                    <h1>Nuevo mensaje desde portafolio</h1>
                        <ul>
                            <li>{name}</li>
                            <li>{subject}</li>
                            <li>{email}</li>
                        </ul>
                    </div>"""

    mail.send(msg)
    return "Email  enviado correctamente"
