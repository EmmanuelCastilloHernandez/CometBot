# THIS IS THE SCRIPT HELPING TO KEEP THE BOT ALIVE W/O HUMAN
# INFERFERENCE
from flask import Flask, render_template
from threading import Thread
import os

websiteImgs = os.path.join('static', 'photoToRender')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = websiteImgs

@app.route('/')
def home():
  imageToShow = os.path.join(app.config['UPLOAD_FOLDER'], 'CometLogo.jpg')
  return render_template('index.html', user_image=imageToShow)

@app.route('/features')
def featuresPage():
  return render_template('features.html')

@app.route('/versions')
def versionsPage():
  return render_template('versions.html')

@app.route('/creators')
def creatorsPage():
  return render_template('creators.html')

def run():
  app.run(host='0.0.0.0',port=8080)

def dontDieOnMe():
  t = Thread(target=run)
  t.start()