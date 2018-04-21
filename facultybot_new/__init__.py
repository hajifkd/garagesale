from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, instance_relative_config=True, static_url_path='')
app.config.from_object('config')
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

from facultybot_new.controllers import api

app.register_blueprint(api, url_prefix="/api/v1")

@app.route('/')
def root():
    return app.send_static_file('index.html')
