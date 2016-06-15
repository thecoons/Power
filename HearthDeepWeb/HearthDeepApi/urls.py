from django.conf.urls import url
from HearthDeepApi import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^hearthlog/$', views.HearthLogList.as_view()),
    url(r'^hearthlog/(?P<pk>[0-9]+)/$', views.HearthLogDetail.as_view()),
    # url(r'^logupload/$', views.LogUploadList.as_view()),
    # url(r'^logupload/(?P<pk>[0-9]+)/$', views.LogUploadDetail.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
