from flask import Blueprint, render_template


views = Blueprint('views', __name__, template_folder='tem[lates')

@views.route('/')
def hello_world():
  name = 'Victor'
  return render_template('index.html', name=name)

@views.route('/menu')
def menu():
  return render_template('menu.html')

@views.route('/login')
def login():
  return render_template('login.html')
