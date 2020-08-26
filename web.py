from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
  return "Audray Gyau is a smart kid"
