from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from geoalchemy2.types import Geometry
import geoalchemy2.functions as func
import psycopg2
import models


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://Web:web@localhost/flaskmusic'
db = SQLAlchemy(app)
app.debug = True



@app.route('/')
def layers_point():
    conn = psycopg2.connect("dbname='flaskmusic' user='Web'host='localhost' password='web'")
    cur = conn.cursor()
    a = '''SELECT* FROM firehydjson UNION ALL SELECT* FROM sysvalvejson'''
    cur.execute(a)
    jsonlist = cur.fetchall()
    return render_template('map.html', jsonlist=jsonlist)


if __name__ == "__main__":
    app.run()