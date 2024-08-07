from . import views
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
        path('',views.admin_login,name='admin-login'),
        path('dashboard', views.dashboard, name='dashboard'),
        path('Blog', views.blog, name='Blog'),
        path('logout',views.logout_admin, name='logout'),
        path('create_blog',views.create_blog, name='create_blog'),
        path('status',views.status, name='status'),
        path('descriptionn',views.description_blog, name='descriptionn'),
        path('edit_blog',views.edit_blog, name='edit_blog'),
        path('edit_blog_action',views.edit_blog_action,name='edit_blog_action'),
        path('delete-blog',views.delete_blog,name='delete-blog'),
        path('delete-img',views.delete_img,name='delete-img'),
        path('check-box',views.check_box,name='check-box')

]        

  

