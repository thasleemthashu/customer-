from django.conf.urls import url
from . import views
app_name = 'agent'
urlpatterns = [
    url(r'^$', views.index, name = "index") ,
    url(r'^$', views.address, name = "address"),

]
