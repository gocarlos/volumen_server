"""django_volumen URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

# Import the new view we created
from volumen_main_app.views import HomeView
from volumen_status_app.views import StatusView
from podcast_browser_app.views import BrowseView
from user_management_app.views import UserView
from player_app.views import PlayerView

urlpatterns = [
url(r'^$', HomeView.as_view()),
    url(r'^admin/', admin.site.urls),
    url(r'^status/', StatusView.as_view()),
    url(r'^browse/', BrowseView.as_view()),
    url(r'^user/', UserView.as_view()),
    url(r'^player/', PlayerView.as_view()),
]
