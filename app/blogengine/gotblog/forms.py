from django import forms
from django.core.exceptions import ValidationError
import re

from .models import *
from .domains import *

class UserForm(forms.Form):
	login = forms.CharField(required = True, widget = forms.TextInput(attrs = {'class' : 'form-control'}), label = 'Логин')
	hash_password = forms.CharField(required = True, widget = forms.TextInput(attrs = {'class' : 'form-control'}), label = 'Пароль')

class PostForm(forms.Form):
	user_id = forms.IntegerField(required = True, widget = forms.NumberInput(attrs = {'class' : 'form-control'}), label = 'Id пользователя', min_value = 1)
	title = forms.CharField(required = True, widget = forms.TextInput(attrs = {'class' : 'form-control'}), label = 'Заголовок')
	body = forms.CharField(required = True, widget = forms.Textarea(attrs = {'class' : 'form-control'}), label = 'Текст')
	publication_date = forms.DateField(required = True, widget = forms.DateInput(attrs = {'class' : 'form-control'}), label = 'Дата публикации')

	def clean_user_id(self):
		data = self.cleaned_data['user_id']

		if UserModel.get(data) == None:
			raise ValidationError('Данного пользователя не существует')

		return data

class CommentForm(forms.Form):
	user_id = forms.IntegerField(required = True, widget = forms.NumberInput(attrs = {'class' : 'form-control',}), label = 'Id пользователя', min_value = 1)
	post_id = forms.IntegerField(required = True, widget = forms.NumberInput(attrs = {'class' : 'form-control'}), label = 'Id поста', min_value = 1)
	body = forms.CharField(required = True, widget = forms.Textarea(attrs = {'class' : 'form-control'}), label = 'Текст')
	publication_date = forms.DateField(required = True, widget = forms.DateInput(attrs = {'class' : 'form-control'}), label = 'Дата публикации')

	def clean_user_id(self):
			data = self.cleaned_data['user_id']

			if UserModel.get(data) == None:
				raise ValidationError('Данного пользователя не существует')

			return data

	def clean_post_id(self):
			data = self.cleaned_data['post_id']

			if UserModel.get(data) == None:
				raise ValidationError('Данного поста не существует')

			return data

class SubscriberForm(forms.Form):
	user_id = forms.IntegerField(required = True, widget = forms.NumberInput(attrs = {'class' : 'form-control'}), label = 'Id пользователя', min_value = 1)
	subscriber_id = forms.IntegerField(required = True, widget = forms.NumberInput(attrs = {'class' : 'form-control'}), label = 'Id подписчика', min_value = 1)

	def clean_user_id(self):
			data = self.cleaned_data['user_id']

			if UserModel.get(data) == None:
				raise ValidationError('Данного пользователя не существует')

			return data

	def clean_subscriber_id(self):
			data = self.cleaned_data['subscriber_id']

			if UserModel.get(data) == None:
				raise ValidationError('Данного пользователя не существует')

			return data