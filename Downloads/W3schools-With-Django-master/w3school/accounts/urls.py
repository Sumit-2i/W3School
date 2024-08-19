from django.urls import path
from django.contrib.auth import views as auth_view
from . import views as core_view

app_name = 'accounts'

urlpatterns = [
  path(r'^login/$', auth_view.LoginView.as_view(template_name='accounts/login.html'), name='login'),
  path(r'^logout/$', auth_view.LogoutView.as_view(), name='logout'),
  path(r'^signup/$', core_view.Signup.as_view(), name='signup'),
  path(r'^$', core_view.UserList.as_view(), name='list_user_api'),
  path(r'^(?P<pk>[0-9]+)/$', core_view.UserDetail.as_view(), name='detail_user_api'),
]
