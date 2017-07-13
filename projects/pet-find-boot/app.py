from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://pet-find-boot:fhyBwcgZHHGiMj53@localhost:8889/pet-find-boot"
app.config["SQLALCHEMY_ECHO"] = True
db = SQLAlchemy(app)