from typing import Collection
import pymongo
from pymongo import MongoClient
from distutils.text_file import TextFile
from  flask import Flask, render_template, session, redirect,url_for
from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,PasswordField

from wtforms.validators import DataRequired

cluster = MongoClient("mongodb+srv://alaska:asdfghjkl123@cluster0.lzlbk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db =cluster['login']
Collection = db['username']
user=''
pas=''
app = Flask(__name__)

app.config['SECRET_KEY']  = 'mykey'

class infoform(FlaskForm):
    username = StringField('What breed are you?')
    password = PasswordField('Password')
    submit = SubmitField('Submit')


@app.route('/', methods=['GET','POST'])
def index():
    form = infoform()
    if form.validate_on_submit():
        session['username'] = form.username.data
        session['password'] = form.password.data
        Collection.insert_one({session['username']:session['password']})
        return redirect(url_for('Home'))
    return render_template('login.html',form=form)
@app.route('/Home')
def Home():
    return render_template('Home.html')

if __name__ == '__main__':
    app.run(debug=True)
