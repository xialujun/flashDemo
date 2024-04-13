# from flask import Flask, render_template, url_for
# from markupsafe import escape
#
# app = Flask(__name__)
#
# # @app.route('/user/<name>')
# # def user_page(name):
# #     return f'user:{escape(name)}'
#
# @app.route('/')
# def hello():
#     return 'hello'
#
# # @app.route('/test')
# # def test_url_for():
# #     print(url_for('hello'))
# #     print(url_for('user_page', name='lili'))
# #     print(url_for('user_page', name='lici'))
# #     print(url_for('test_url_for'))
# #     print(url_for('test_url_for', num=2))
# #     print(url_for('static', filename='favicon.ico'))
# #     return 'Test page'
#
#
# name = 'lujun'
# movies = [
#     {'title': 'My Neighbor Totoro', 'year': '1988'},
#     {'title': 'Dead Poets Society', 'year': '1989'},
#     {'title': 'A Perfect World', 'year': '1993'},
#     {'title': 'Leon', 'year': '1994'},
#     {'title': 'Mahjong', 'year': '1996'},
#     {'title': 'Swallowtail Butterfly', 'year': '1996'},
#     {'title': 'King of Comedy', 'year': '1999'},
#     {'title': 'Devils on the Doorstep', 'year': '1999'},
#     {'title': 'WALL-E', 'year': '2008'},
#     {'title': 'The Pork of Music', 'year': '2012'},
# ]
#
# app = Flask(__name__)
# @app.route('/')
# def index():
#     return render_template('index.html', name=name, movies=movies)


import os.path
import sys

import click
from flask import Flask, current_app, render_template
from flask_sqlalchemy import SQLAlchemy



WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'


app = Flask(__name__)
with app.app_context():
    a = current_app
    print(a)
# ctx = app.app_context()
# ctx.push()
# a = current_app
# ctx.pop()

app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(app.root_path, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

with app.app_context():
    a = current_app
    print(a)
    db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60))
    year = db.Column(db.String(4))



@app.cli.command()
@click.option('--drop', is_flag=True,help='Create after drop.')
def initdb(drop):
    if drop:
        db.drop_all()
    db.create_all()
    click.echo('Initialized database.')

@app.route('/')
def index():
    movies = Movie.query.all()
    print(len(movies))
    return render_template('index.html',  movies=movies)

@app.cli.command("forge")
def forge():
    """Generate fake data."""
    db.create_all()

    name = 'lujun'
    movies = [
        {'title': 'My Neighbor Totoro', 'year': '1988'},
        {'title': 'Dead Poets Society', 'year': '1989'},
        {'title': 'A Perfect World', 'year': '1993'},
        {'title': 'Leon', 'year': '1994'},
        {'title': 'Mahjong', 'year': '1996'},
        {'title': 'Swallowtail Butterfly', 'year': '1996'},
        {'title': 'King of Comedy', 'year': '1999'},
        {'title': 'Devils on the Doorstep', 'year': '1999'},
        {'title': 'WALL-E', 'year': '2008'},
        {'title': 'The Pork of Music', 'year': '2012'},
    ]

    user = User(name=name)
    db.session.add(user)
    for m in movies:
        movie = Movie(title=m['title'], year=m['year'])
        db.session.add(movie)

    db.session.commit()
    click.echo('Done.')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.context_processor
def inject_user():
    user = User.query.filter_by(name='lujun').first()
    return dict(user=user)





