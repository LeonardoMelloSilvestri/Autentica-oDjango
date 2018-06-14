from django.urls import path
from .views import index, register

urlpatterns = [
	path('', index, name='url_index'),
	path('accounts/register', register, name='url_register')
]