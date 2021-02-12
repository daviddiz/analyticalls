from django.conf.urls import url 
from importJson import views 
 
urlpatterns = [ 
    url(r'^api/importJson$', views.retreived_data_list),
    url(r'^api/importJson/(?P<pk>[0-9]+)$', views.retreived_data_detail),
    url(r'^api/importJson/all$', views.retreived_data_list_all)
]
