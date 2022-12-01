from flask import Flask
import requests
import time
app = Flask(__name__)

@app.route("/")

def home():

    return "wtf"