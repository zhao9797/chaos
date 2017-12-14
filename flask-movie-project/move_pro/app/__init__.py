#coding:utf8
from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
import os
import pymysql

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:4313885265@localhost:3306/movie"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SECRET_KEY"]='7d75c37dde1a4be8bbe9af254e0475ff'
app.config["UP_DIR"]=os.path.join(os.path.abspath(os.path.dirname(__file__)),"static/uploads/")
app.config["FC_DIR"]=os.path.join(os.path.abspath(os.path.dirname(__file__)),"static/uploads/users/")
app.debug = False
db = SQLAlchemy(app)

from app.home import home as home_blueprint
from app.admin import admin as admin_blueprint

app.register_blueprint(home_blueprint)
app.register_blueprint(admin_blueprint, url_prefix="/admin")

@app.errorhandler(404)
def page_not_found(error):
    return render_template("home/404.html"),404
