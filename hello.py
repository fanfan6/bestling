# coding=utf8

from flask import Flask, render_template
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)


@app.route('/')
def index():
    return '<h1>hello everyone</h1>'


@app.route('/user/<name>')
def user_name(name):
    return render_template('user.html', name=name)


if __name__ == '__main__':
    manager.run()
