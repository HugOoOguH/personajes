"""personajes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from heroes import views
#from posts import views as views2
from posts import urls as postsUrls
from heroes import urls as heroesUrls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^',include(heroesUrls,namespace='wolverine')),
    #url(r'^wolverine/$', views.Spider.as_view()),
    url(r'^blog/',include(postsUrls, namespace='posts')),
    #url(r'^blog/$',views2.ListView.as_view()),
    
    #url(r'^detalle/(?P<id>\d+)/$',
    #    views2.DetailView.as_view(),
   #     name="detalle"),
    #url(r'^blog/$',views2.Blog.as_view()),
]
