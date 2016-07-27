from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^wolverine/$', views.Spider.as_view(),name="heroes"),
]