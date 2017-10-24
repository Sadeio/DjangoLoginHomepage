from django.conf.urls import url
from . import views #Look in folder in the level of account and homepage for a views file
from django.contrib.auth.views import login
urlpatterns = [
    url(r'^$', views.home),
    url(r'^login/$', login, {'template_name': 'accounts/login.html'})
]