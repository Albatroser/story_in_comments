from django.conf.urls import url

from glue import views


urlpatterns = [
    url(r'^communities/$', views.communities, name="communities"),
    url(r'^adding/$', views.adding, name="adding"),
]
