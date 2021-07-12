from application import app, db
from flask_login import (LoginManager,UserMixin,login_user,login_required,
logout_user,current_user)
from datetime import datetime

class User(db.Model,UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(55), nullable=False)
	email = db.Column(db.String(55), nullable=False)
	password = db.Column(db.String(200))
	user_image = db.Column(db.Text,nullable=False)
	post = db.relationship('Posts',backref='user',lazy='dynamic')
	reply = db.relationship('Replies',backref='user',lazy='dynamic')

class Posts(db.Model):
	post_id = db.Column(db.Integer, primary_key=True)
	post_title = db.Column(db.String(250), nullable=False)
	content = db.Column(db.Text, nullable=False)
	post_date = db.Column(db.DateTime(timezone=True), nullable=False)
	user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
	post = db.relationship('Replies',backref='posts',lazy='dynamic')

class Replies(db.Model):
    reply_id = db.Column(db.Integer, primary_key=True)
    reply_body = db.Column(db.String(250), nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    post_id = db.Column(db.Integer,db.ForeignKey('posts.post_id'))