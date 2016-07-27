from django.conf.urls import url
#el punto indica importa deaquimismo
from . import views


urlpatterns = [
	url(r'^$',views.ListView.as_view(), name="blog"), #blog/
	url(r'^nuevo/$', #blog/
        views.NuevoPost.as_view(),
        name="nuevo"),
	url(r'^(?P<slug>[-\w]+)/$', #blog/
        views.DetailView.as_view(),
        name="detalle"),
#	url(r'^(?P<id>\d+)/$', #blog/
   #     views.DetailView.as_view(),
   #     name="detalle"),
]