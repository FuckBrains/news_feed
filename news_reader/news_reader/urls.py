"""news_reader URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from news import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# from django.conf.urls import url
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^news/', include('news.urls')),
    url(r'^short_video/', include('short_video.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^english_tts/', include('english_tts.urls')),
]

# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
#     url('app/', include('aggregate_and_read.urls')),
#
# ]
# from django.contrib import admin
#
# urlpatterns = [
#     path('templates/', include('aggregate_and_read.urls')),
#     path('admin/', admin.site.urls),
# ]