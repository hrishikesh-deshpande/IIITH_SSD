import requests
from flask import Flask, request
from flask_login import (LoginManager, UserMixin, login_manager,
                         login_required, login_user, logout_user)
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
login_manager = LoginManager()


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
app.config['SECRET_KEY'] = 'secretkey'

db.init_app(app)
login_manager.init_app(app)


@app.route('/user/register', methods=['POST'])
def register():
    if(request.method == 'POST'):
        req = request.get_json()
        username = req['username']
        password = req['password']
        check_user = User.query.filter_by(username=username).first()
        if(check_user):
            return 'User already exists'
        else:
            newUser = User(username=username, password=password)
            db.session.add(newUser)
            db.session.commit()
            return 'User successfully registered'


@app.route('/user/login', methods=['POST'])
def login():
    if(request.method == 'POST'):
        req = request.get_json()
        username = req['username']
        password = req['password']
        if(check_user):
            if(check_user.password == password):
                login_user(check_user)
                return 'User logged in successfully'
            else:
                return 'Incorrect password'
        else:
            return 'User does not exist'


@app.route('/user/logout', methods=['POST'])
@login_required
def logout():
    if(request.method == 'POST'):
        req = request.get_json()
        username = req['username']
        logout_user(username)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


if __name__ == "__main__":

    host, port = '127.0.0.1', 50551
    app.run(host=host, port=port)

    with app.app_context():
        db.create_all()
