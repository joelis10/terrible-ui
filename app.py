from flask import Flask, render_template
from random import randint

app = Flask(__name__)


@app.route('/')
def phone_no():

    return render_template("phone-no.html", randint=randint)
