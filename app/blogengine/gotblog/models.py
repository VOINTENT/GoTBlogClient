from django.db import models
from django.shortcuts import reverse

# Create your models here.
class User(models.Model):
	login = models.CharField(max_length = 150, unique = True)
	password = models.CharField(max_length = 150)

	def __str__(self):
		return self.login

	def get_absolute_url(self):
		return reverse('user_id_url', kwargs = {'id' : self.id})

	def get_update_url(self):
		return reverse('user_update_url', kwargs = {'id' : self.id})

	def get_delete_url(self):
		return reverse('user_delete_url', kwargs = {'id' : self.id})

class Post(models.Model):
	user = models.ForeignKey('User', on_delete = models.CASCADE)
	title = models.CharField(max_length = 150, default = 'Без названия')
	body = models.TextField(db_index = True)
	date_pub = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return self.body

	def get_absolute_url(self):
		return reverse('post_id_url', kwargs = {'id' : self.id})

	def get_update_url(self):
		return reverse('post_update_url', kwargs = {'id' : self.id})

	def get_delete_url(self):
		return reverse('post_delete_url', kwargs = {'id' : self.id})

class Comment(models.Model):
	user = models.ForeignKey('User', on_delete = models.CASCADE)
	post = models.ForeignKey('Post', on_delete = models.CASCADE)
	body = models.TextField(db_index = True)
	date_pub = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return self.body

	def get_absolute_url(self):
		return reverse('comment_id_url', kwargs = {'id' : self.id})

	def get_update_url(self):
		return reverse('comment_update_url', kwargs = {'id' : self.id})

	def get_delete_url(self):
		return reverse('comment_delete_url', kwargs = {'id' : self.id})

class Subscriber(models.Model):
	user = models.ForeignKey('User', on_delete = models.CASCADE, related_name = 'users')
	subscriber = models.ForeignKey('User', on_delete = models.CASCADE, related_name = 'subscribers')

	def __str__(self):
		return self.login + " - " + self.subscriber

	def get_absolute_url(self):
		return reverse('subscriber_id_url', kwargs = {'id' : self.id})

	def get_update_url(self):
		return reverse('subscriber_update_url', kwargs = {'id' : self.id})

	def get_delete_url(self):
		return reverse('subscriber_delete_url', kwargs = {'id' : self.id})