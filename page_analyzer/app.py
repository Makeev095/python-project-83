from flask import Flask
import os
from dotenv import load_dotenv

load_dotenv()
os.getenv("PORT")

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'
