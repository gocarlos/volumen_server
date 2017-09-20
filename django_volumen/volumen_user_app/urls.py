from django.conf.urls import url
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from . import views
from views import UserProfileView

# urlpatterns = [
#     url(r'^$', views.index, name='index'),
#     url(r'^signup/$', views.signup, name='signup'),
#     url(r'^login/$', views.login, name='login'),
#     url(r'^logout/$', views.logout, name='logout'),
#     # url(r'^(?P<username>\w+)/', views.user_account, name='user_account'),
# ]


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    # By user ID
    url(r'^id/(?P<pk>\d+)/$', UserProfileView.as_view()),
    # By username
    url(r'^(?P<slug>[\w.@+-]+)/$', UserProfileView.as_view()),
]
