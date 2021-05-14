# THIS IS THE SCRIPT HELPING TO KEEP THE BOT ALIVE W/O HUMAN
# INFERFERENCE
from flask import Flask, render_template
from threading import Thread

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

def run():
  app.run(host='0.0.0.0',port=8080)

def dontDieOnMe():
    t = Thread(target=run)
    t.start()