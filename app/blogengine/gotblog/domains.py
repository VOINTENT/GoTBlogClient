import requests
import json
from django.shortcuts import reverse

class UserModel:
	def __init__(self, dict):
		self.id = dict.get('id')
		self.login = dict.get('login')
		self.hash_password = dict.get('hash_password')

	def get(id):
		r = requests.get('http://127.0.0.1:5000/user/' + str(id))
		if r.text == 'Failed':
			return None
		return UserModel(r.json())

	def all():
		r = requests.get('http://127.0.0.1:5000/user')

		users = []
		for dict in r.json():
			users.append(UserModel(dict))
		return users

	def post(user):
		r = requests.post(
			'http://127.0.0.1:5000/user', 
			data = json.dumps(user.to_dict(), ensure_ascii = False).encode('utf-8')
		)
		if r.text == 'Failed':
			return None
		return UserModel(r.json())

	def update(user):
		r = requests.put(
			'http://127.0.0.1:5000/user/' + str(user.id), 
			data = json.dumps(user.to_dict(), ensure_ascii = False).encode('utf-8')
		)
		if r.text == 'Failed':
			return None
		return UserModel(r.json())

	def delete(user):
		r = requests.delete(
			'http://127.0.0.1:5000/user/' + str(user.id), 
			data = json.dumps(user.to_dict(), ensure_ascii = False).encode('utf-8')
		)
		if r.text == 'Failed':
			return None
		return UserModel(r.json())

	def to_dict(self):
		dict = {
			'id' : self.id,
			'login' : self.login,
			'hash_password' : self.hash_password
		}
		return dict

	def get_absolute_url(self):
		return reverse('user_id_url', kwargs = {'id' : self.id})

	def get_update_url(self):
		return reverse('user_update_url', kwargs = {'id' : self.id})

	def get_delete_url(self):
		return reverse('user_delete_url', kwargs = {'id' : self.id})

	def __str__(self):
		return self.login

	def name():
		return 'User'

class PostModel:
	def __init__(self, dict):
		self.id = dict.get('id')
		self.user = UserModel.get(dict.get('user_id'))
		self.title = dict.get('title')
		self.body = dict.get('body')
		self.publication_date = dict.get('publication_date')

	def get(id):
		r = requests.get('http://127.0.0.1:5000/post/' + str(id))
		if r.text == 'Failed':
			return None
		return PostModel(r.json())

	def all():
		r = requests.get('http://127.0.0.1:5000/post')

		posts = []
		dict = r.json()
		for i in range(0, 100):
			posts.append(PostModel(dict[i]))
		return posts

	def post(post):
		r = requests.post(
			'http://127.0.0.1:5000/post', 
			data = json.dumps(post.to_dict(), ensure_ascii = False).encode('utf-8')
		)
		if r.text == 'Failed':
			return None
		return PostModel(r.json())

	def update(post):
		r = requests.put(
			'http://127.0.0.1:5000/post/' + str(post.id), 
			data = json.dumps(post.to_dict(), ensure_ascii = False).encode('utf-8')
		)
		if r.text == 'Failed':
			return None
		return PostModel(r.json())

	def delete(post):
		r = requests.delete(
			'http://127.0.0.1:5000/post/' + str(post.id), 
			data = json.dumps(post.to_dict(), ensure_ascii = False).encode('utf-8')
		)
		if r.text == 'Failed':
			return None
		return PostModel(r.json())

	def to_dict(self):
		dict = {
			'id' : self.id,
			'user_id' : self.user.id,
			'title' : self.title,
			'body' : self.body,
			'publication_date' : str(self.publication_date)
		}
		return dict

	def get_absolute_url(self):
		return reverse('post_id_url', kwargs = {'id' : self.id})

	def get_update_url(self):
		return reverse('post_update_url', kwargs = {'id' : self.id})

	def get_delete_url(self):
		return reverse('post_delete_url', kwargs = {'id' : self.id})

	def __str__(self):
		return self.title

	def name():
		return 'Post'

class CommentModel:
	def __init__(self, dict):
		self.id = dict.get('id')
		self.user = UserModel.get(dict['user_id'])
		self.post = PostModel.get(dict['post_id'])
		self.body = dict['body']
		self.publication_date = dict['publication_date']

	def get(id):
		r = requests.get('http://127.0.0.1:5000/comment/' + str(id))
		if r.text == 'Failed':
			return None
		return CommentModel(r.json())

	def all():
		r = requests.get('http://127.0.0.1:5000/comment')

		comments = []
		dict = r.json()
		for i in range(0, 100):
			comments.append(CommentModel(dict[i]))
		return comments

	def post(comment):
		r = requests.post(
			'http://127.0.0.1:5000/comment', 
			data = json.dumps(comment.to_dict(), ensure_ascii = False).encode('utf-8')
		)
		if r.text == 'Failed':
			return None
		return CommentModel(r.json())

	def update(comment):
		r = requests.put(
			'http://127.0.0.1:5000/comment/' + str(comment.id), 
			data = json.dumps(comment.to_dict(), ensure_ascii = False).encode('utf-8')
		)
		if r.text == 'Failed':
			return None
		return CommentModel(r.json())

	def delete(comment):
		r = requests.delete(
			'http://127.0.0.1:5000/comment/' + str(comment.id), 
			data = json.dumps(comment.to_dict(), ensure_ascii = False).encode('utf-8')
		)
		if r.text == 'Failed':
			return None
		return CommentModel(r.json())

	def to_dict(self):
		dict = {
			'id' : self.id,
			'user_id' : self.user.id,
			'post_id' : self.post.id,
			'body' : self.body,
			'publication_date' : self.publication_date
		}
		return dict

	def get_absolute_url(self):
		return reverse('comment_id_url', kwargs = {'id' : self.id})

	def get_update_url(self):
		return reverse('comment_update_url', kwargs = {'id' : self.id})

	def get_delete_url(self):
		return reverse('comment_delete_url', kwargs = {'id' : self.id})

	def __str__(self):
		return self.body

	def name():
		return 'Comment'


class SubscriberModel:
	def __init__(self, dict):
		self.id = dict.get('id')
		self.user = UserModel.get(dict['user_id'])
		self.subscriber = UserModel.get(dict['subscriber_id'])

	def get(id):
		r = requests.get('http://127.0.0.1:5000/subscriber/' + str(id))
		if r.text == 'Failed':
			return None
		return SubscriberModel(r.json())

	def all():
		r = requests.get('http://127.0.0.1:5000/subscriber')

		subscribers = []
		dict = r.json()
		for i in range(0, 100):
			subscribers.append(SubscriberModel(dict[i]))
		return subscribers

	def post(subscriber):
		r = requests.post(
			'http://127.0.0.1:5000/subscriber', 
			data = json.dumps(subscriber.to_dict(), ensure_ascii = False).encode('utf-8')
		)
		if r.text == 'Failed':
			return None
		return SubscriberModel(r.json())

	def update(subscriber):
		r = requests.put(
			'http://127.0.0.1:5000/subscriber/' + str(subscriber.id), 
			data = json.dumps(subscriber.to_dict(), ensure_ascii = False).encode('utf-8')
		)
		if r.text == 'Failed':
			return None
		return SubscriberModel(r.json())

	def delete(subscriber):
		r = requests.delete(
			'http://127.0.0.1:5000/subscriber/' + str(subscriber.id), 
			data = json.dumps(subscriber.to_dict(), ensure_ascii = False).encode('utf-8')
		)
		if r.text == 'Failed':
			return None
		return SubscriberModel(r.json())

	def to_dict(self):
		dict = {
			'id' : self.id,
			'user_id' : self.user.id,
			'subscriber_id' : self.subscriber.id
		}
		return dict

	def get_absolute_url(self):
		return reverse('subscriber_id_url', kwargs = {'id' : self.id})

	def get_update_url(self):
		return reverse('subscriber_update_url', kwargs = {'id' : self.id})

	def get_delete_url(self):
		return reverse('subscriber_delete_url', kwargs = {'id' : self.id})

	def __str__(self):
		return (str(self.user) + " - " + str(self.subscriber))

	def name():
		return 'Subscriber'

