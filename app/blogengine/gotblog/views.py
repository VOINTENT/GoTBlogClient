from django.shortcuts import render
from django.views.generic import View

from .utils import *
from .domains import *
from .forms import *

# Create your views here.
def index(request):
	return render(request, 'gotblog/index.html')

class UserList(ObjectListMixin, View):
	model = UserModel
	template = 'gotblog/users.html'

class UserId(ObjectIdMixin, View):
	model = UserModel
	template = 'gotblog/user_detail.html'

class UserCreate(ObjectCreateMixin, View):
	model = UserModel
	model_form = UserForm
	template = 'gotblog/user_create.html'

class UserUpdate(ObjectUpdateMixin, View):
	model = UserModel
	model_form = UserForm
	template = 'gotblog/user_update.html'

class UserDelete(ObjectDeleteMixin, View):
	model = UserModel
	template = 'gotblog/user_delete.html'
	redirect_url = 'user_url'



class PostList(ObjectListMixin, View):
	model = PostModel
	template = 'gotblog/posts.html'

class PostId(ObjectIdMixin, View):
	model = PostModel
	template = 'gotblog/post_detail.html'

class PostCreate(ObjectCreateMixin, View):
	model = PostModel
	model_form = PostForm
	template = 'gotblog/post_create.html'

class PostUpdate(ObjectUpdateMixin, View):
	model = PostModel
	model_form = PostForm
	template = 'gotblog/post_update.html'

class PostDelete(ObjectDeleteMixin, View):
	model = PostModel
	template = 'gotblog/post_delete.html'
	redirect_url = 'post_url'

	

class CommentList(ObjectListMixin, View):
	model = CommentModel
	template = 'gotblog/comments.html'

class CommentId(ObjectIdMixin, View):
	model = CommentModel
	template = 'gotblog/comment_detail.html'

class CommentCreate(ObjectCreateMixin, View):
	model = CommentModel
	model_form = CommentForm
	template = 'gotblog/comment_create.html'

class CommentUpdate(ObjectUpdateMixin, View):
	model = CommentModel
	model_form = CommentForm
	template = 'gotblog/comment_update.html'

class CommentDelete(ObjectDeleteMixin, View):
	model = CommentModel
	template = 'gotblog/comment_delete.html'
	redirect_url = 'comment_url'



class SubscriberList(ObjectListMixin, View):
	model = SubscriberModel
	template = 'gotblog/subscribers.html'

class SubscriberId(ObjectIdMixin, View):
	model = SubscriberModel
	template = 'gotblog/subscriber_detail.html'

class SubscriberCreate(ObjectCreateMixin, View):
	model = SubscriberModel
	model_form = SubscriberForm
	template = 'gotblog/subscriber_create.html'

class SubscriberUpdate(ObjectUpdateMixin, View):
	model = SubscriberModel
	model_form = SubscriberForm
	template = 'gotblog/subscriber_update.html'

class SubscriberDelete(ObjectDeleteMixin, View):
	model = SubscriberModel
	template = 'gotblog/subscriber_delete.html'
	redirect_url = 'subscriber_url'
