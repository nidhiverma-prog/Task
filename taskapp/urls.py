from .views import hello,register,login_view,logout_view,employe,users,admins,add_emp,create_post
from django.conf.urls import url

app_name='taskapp'

urlpatterns = [
    
    url(r'^$',hello, name="hello"),
    url('emp/',employe,name='employe'),
    # url('login/emp/',login_view,name='login_view_emp'),
    url('users/',users,name='users'),
    # url('ajax-posting/', ajax_posting, name='ajax_posting')
    # url('create_post/',create_post,name='create_post'),
    url('admins/',admins,name='admins'),
    url('login/',login_view, name='login'),
    url('register/',register, name='register'),
    url('logout/',logout_view, name='logout'),

]