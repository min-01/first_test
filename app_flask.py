from flask import Flask, render_template, request
from end_mysql import User, Thing, getuser

# from wtforms import Form, TextField, PasswordField, validators

app = Flask(__name__)
# name = 'name'
# id = 'id'
# sex = 'sex'
# grade = 'grade'
# tel = 'tel'
# email = 'email'
# choose_location = 'choose_location'
# introduce_myself = 'introduce_myself'


@app.route('/index')
def index():
    return render_template('index1.html')


@app.route('/')
def index1():
    return render_template('index1.html')


@app.route('/apply', methods=['POST'])
def apply():
    name = request.form['name']
    id = request.form['id']
    sex = request.form['sex']
    grade = request.form['grade']
    tel = request.form['tel']
    email = request.form['email']
    choose_location = request.form['choose_location']
    introduce_yourself = request.form['introduce_yourself']
    # create_namelist()
    User.add_one(id, name, sex, grade, tel, email, choose_location, introduce_yourself)
    print("name:%s id:%s" % (name, id))
    return render_template("index1.html")


@app.route('/name_list')
def name_list():
    users = User.query_all()
    return render_template("list.html", users=users)


@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/todo', methods=['GET', 'POST'])
def todo():
    # thing = request.form['thing']
    # Thing.add_todo(thing)
    things = Thing.query_thing()
    return render_template('todo.html', things=things)


@app.route('/add_todo', methods=['GET', 'POST'])
def add_todo():
    thing = request.form['thing']
    Thing.add_todo(thing)
    things = Thing.query_thing()
    return render_template('todo.html', things=things)


@app.route('/loging', methods=['GET', 'POST'])
def loging():
    # thing = getuser()
    account = request.form['inputEmail']
    password = request.form['inputPassword']
    getuser.set(account, password)
    things = Thing.query_thing()
    return render_template('todo.html', things=things)