from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator

from .models import *

class ObjectListMixin:
	model = None
	template = None

	def get(self, request):
		objects = self.model.all()

		paginator = Paginator(objects, 10)

		page_number = request.GET.get('page', 1)
		page = paginator.get_page(page_number)

		is_paginated = page.has_other_pages()

		if page.has_previous():
			prev_url = '?page={}'.format(page.previous_page_number())
		else:
			prev_url = ''

		if page.has_next():
			next_url = '?page={}'.format(page.next_page_number())
		else:
			next_url = ''

		context = {
			'page_object' : page,
			'is_paginated' : is_paginated,
			'next_url': next_url,
			'prev_url' : prev_url
		}
		return render(request, self.template, context = context)

class ObjectIdMixin:
	model = None
	template = None

	def get(self, request, id):
		obj = self.model.get(id)
		context = {
			self.model.name().lower() : obj, 
			'admin_object' : obj, 
			'detail' : True
		}
		
		return render(request, self.template, context = context)

class ObjectCreateMixin:
	model_form = None
	template = None

	def get(self, request):
		form = self.model_form()
		return render(request, self.template, context = {'form' : form})

	def post(self, request):
		bound_form = self.model_form(request.POST)
		obj = self.model(request.POST)
		if bound_form.is_valid():
			new_obj = self.model.post(obj)
			return redirect(new_obj.get_absolute_url())
		return render(request, self.template, context = {'form' : bound_form})
	
class ObjectUpdateMixin:
	model = None
	model_form = None
	template = None

	def get(self, request, id):
		obj = self.model.get(id)
		bound_form = self.model_form(obj.to_dict())

		context = {
			'form' : bound_form, 
			self.model.__name__.lower() : obj
		}

		return render(request, self.template, context = context)

	def post(self, request, id):
		bound_form = self.model_form(request.POST)

		new_obj = self.model(request.POST)
		obj = self.model.get(id)
		new_obj.id = obj.id

		if bound_form.is_valid():
			new_obj = self.model.update(new_obj)
			print(new_obj)
			print(type(new_obj))
			return redirect(new_obj.get_absolute_url())

		context = {
			'form' : bound_form, 
			self.model.__name__.lower() : obj
		}

		return render(request, self.template, context = context)

class ObjectDeleteMixin:
	model = None
	template = None
	redirect_url = None

	def get(self, request, id):
		obj = self.model.get(id)
		print(obj)
		print(self.model.__name__.lower())
		return render(request, self.template, context = {self.model.name().lower() : obj})

	def post(self, request, id):
		obj = self.model.get(id)
		res = self.model.delete(obj)
		return redirect(reverse(self.redirect_url))