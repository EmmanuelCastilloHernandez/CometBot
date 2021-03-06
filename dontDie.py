# THIS IS THE SCRIPT HELPING TO KEEP THE BOT ALIVE W/O HUMAN
# INFERFERENCE
from flask import Flask, render_template
import json
from threading import Thread
import os

websiteImgs = os.path.join('static', 'photoToRender')

with open('serverCount.json', 'r') as serverCount:
  serverData = json.load(serverCount)

serverNum = int(serverData["server count"])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = websiteImgs
allowedExtensions = set(['png', 'jpg', 'jpeg', 'gif'])

@app.route('/')
def home():
  imageToShow = os.path.join(app.config['UPLOAD_FOLDER'], 'favicon.png')
  return render_template('index.html', user_image=imageToShow, value=serverNum)

@app.route('/features')
def featuresPage():
  imageToShow = os.path.join(app.config['UPLOAD_FOLDER'], 'favicon.png')
  return render_template('features.html', user_image=imageToShow)

@app.route('/versions')
def versionsPage():
  imageToShow = os.path.join(app.config['UPLOAD_FOLDER'], 'favicon.png')
  return render_template('versions.html', user_image=imageToShow)

@app.route('/creators')
def creatorsPage():
  imageToShow = os.path.join(app.config['UPLOAD_FOLDER'], 'favicon.png')
  return render_template('creators.html', user_image=imageToShow)

@app.route('/invite')
def invitePage():
  imageToShow = os.path.join(app.config['UPLOAD_FOLDER'], 'favicon.png')
  return render_template('invite.html', user_image=imageToShow)

def run():
  app.run(host='0.0.0.0',port=8080)

def dontDieOnMe():
  t = Thread(target=run)
  t.start()