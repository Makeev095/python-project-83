from flask import Flask
import os
from dotenv import load_dotenv


dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'
