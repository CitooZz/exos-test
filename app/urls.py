from django.conf.urls import url
from app.views import UserListView, UserCreateView, UserDeleteView, UserEditView, UserDetailView, \
    UserExportView


urlpatterns = [
    url(r'^users/$', UserListView.as_view(), name='user_list'),
    url(r'^users/export/$', UserExportView.as_view(), name='user_export'),
    url(r'^users/create/$', UserCreateView.as_view(), name='user_create'),
    url(r'^users/(?P<pk>[0-9]+)/$', UserDetailView.as_view(), name='user_detail'),
    url(r'^users/(?P<pk>[0-9]+)/edit/$', UserEditView.as_view(), name='user_edit'),
    url(r'^users/(?P<pk>[0-9]+)/delete/$', UserDeleteView.as_view(), name='user_delete'),
]
