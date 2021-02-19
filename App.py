import mysql.connector
from flask import Flask, render_template,request,session
import os
from decouple import config

app = Flask(__name__)


'''
db =mysql.connector.connect(
    host = config('HOST'),      
    user = config('USER'),
    passwd = config('PASSWORD'),
    database = config('DATABASE')
) write values of DB in .env file'''
@app.route("/")
def index():
    return render_template("index.html")


app.run( debug=True) 