from django.conf.urls import url
from .views import index
from .views import post_relief_effort
from .views import show
from .views import post_item_request
from .views import relief_efforts_index

urlpatterns = [
    url(r'^$', index),
    url(r'^post_url/$', post_relief_effort, name='post_relief_effort'),
    url(r'^relief_efforts/$', relief_efforts_index, name = 'relief_efforts_index'),
    url(r'^([0-9]+)/$', show, name = 'show'),
    url(r'^([0-9]+)/post_item_request/$', post_item_request, name = 'post_item_request')
]
