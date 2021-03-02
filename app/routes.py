from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm

# export FLASK_ENV=development
# export FLASK_APP=floretta_app.py

@app.route('/')
@app.route('/index')
def index():
   conf = app.config['SECRET_KEY']
   user = {'username': 'Konstantinos22'}
   posts = [
      {
         'author': 'Noula',
         'blog_title': 'This is it, The Last Michael Jackson Concert'
      },
      {
         'author': 'Niki',
         'blog_title': 'Best Souvlaki in Town'
      }
   ]
   return render_template('index.html',title='Caffee-Bar',  user=user, posts=posts, conf=conf)

@app.route('/login', methods=['GET', 'POST'])
def login():
   form = LoginForm()
   if form.validate_on_submit():
      flash('Login requested for User {}, remember_me={}'.format(form.username.data, form.remember_me.data))
      return redirect('/index')
   return render_template('login.html', title="Sign In33", form=form)