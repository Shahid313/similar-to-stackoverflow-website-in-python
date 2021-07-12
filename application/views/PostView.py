from flask_classful import FlaskView, route
from application.models.models import *
from flask import render_template, request
from application import db
from flask import redirect, url_for
from application.forms.forms import LoginForm, SignupForm
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import LoginManager,UserMixin,login_user,login_required,logout_user,current_user
from application import login_manager
from sqlalchemy import text

class PostView(FlaskView):
	@route('/home',methods=['GET'])
	def home(self):
		sql = text("SELECT * FROM user RIGHT JOIN posts on posts.user_id = user.id")
		posts = db.engine.execute(sql)
		posts_res = list()
		for post in posts:
			data = dict()
			reply_sql = text("SELECT * FROM replies LEFT JOIN user on user.id = replies.user_id WHERE post_id = "+str(post.post_id))
			post_replies = db.engine.execute(reply_sql)

			data['post_replies'] = post_replies
			data['post_data'] = post

			posts_res.append(data)
		return render_template('index.html', posts_res=posts_res)

	@route('/post_question', methods=['POST'])
	@login_required
	def post_question(self):
		if request.method == 'POST':
			post_title = request.form.get('title')
			post = request.form.get('question')
			new_post = Posts(content=post, post_title=post_title, post_date = datetime.now(), user_id=current_user.id)
			try:
				db.session.add(new_post)
				db.session.commit()
				return redirect(url_for('PostView:home'))
			except e as Exception:
				return "There is an issue in posting"+str(e)

	@route('/reply/<int:id>', methods=['GET','POST'])
	@login_required
	def reply(self, id):
		posts = Posts.query.get_or_404(id)
		if current_user.is_authenticated:
			curr_user = current_user
		if request.method == 'POST':
			reply = request.form.get('question-reply')
			new_reply = Replies(reply_body = reply, user_id = curr_user.id, post_id = posts.post_id)
			db.session.add(new_reply)
			db.session.commit()
			return redirect(url_for('PostView:home'))



				
