from django.urls import path

from .views import *

urlpatterns = [
	path('', index, name = 'index_url'),

	path('users/', UserList.as_view(), name = 'user_url'),
	path('user/create/', UserCreate.as_view(), name = 'user_create_url'),
	path('user/<int:id>/', UserId.as_view(), name = 'user_id_url'),
	path('user/<int:id>/update/', UserUpdate.as_view(), name = 'user_update_url'),
	path('user/<int:id>/delete/', UserDelete.as_view(), name = 'user_delete_url'),
	
	path('posts/', PostList.as_view(), name = 'post_url'),
	path('post/create/', PostCreate.as_view(), name = 'post_create_url'),
	path('post/<int:id>/', PostId.as_view(), name = 'post_id_url'),
	path('post/<int:id>/update/', PostUpdate.as_view(), name = 'post_update_url'),
	path('post/<int:id>/delete/', PostDelete.as_view(), name = 'post_delete_url'),

	path('comments/', CommentList.as_view(), name = 'comment_url'),
	path('comment/create/', CommentCreate.as_view(), name = 'comment_create_url'),
	path('comment/<int:id>/', CommentId.as_view(), name = 'comment_id_url'),
	path('comment/<int:id>/update/', CommentUpdate.as_view(), name = 'comment_update_url'),
	path('comment/<int:id>/delete/', CommentDelete.as_view(), name = 'comment_delete_url'),

	path('subscribers/', SubscriberList.as_view(), name = 'subscriber_url'),
	path('subscriber/create/', SubscriberCreate.as_view(), name = 'subscriber_create_url'),
	path('subscriber/<int:id>/', SubscriberId.as_view(), name = 'subscriber_id_url'),
	path('subscriber/<int:id>/update/', SubscriberUpdate.as_view(), name = 'subscriber_update_url'),
	path('subscriber/<int:id>/delete/', SubscriberDelete.as_view(), name = 'subscriber_delete_url')
]