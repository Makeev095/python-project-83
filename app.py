from flask import Flask


app = Flask(__name__)

@app.route('/hello')
def main():
    return 'Hello, World!'
