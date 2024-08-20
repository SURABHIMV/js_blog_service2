from . import views
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

# urlpatterns = [
#         path('',views.admin_login,name='admin-login'),
#         path('dashboard', views.dashboard, name='dashboard'),
#         path('Blog', views.blog, name='Blog'),
#         path('logout',views.logout_admin, name='logout'),
#         path('create_blog',views.create_blog, name='create_blog'),
#         path('status',views.status, name='status'),
#         path('descriptionn',views.description_blog, name='descriptionn'),
#         path('edit_blog',views.edit_blog, name='edit_blog'),
#         path('edit_blog_action',views.edit_blog_action,name='edit_blog_action'),
#         path('delete-blog',views.delete_blog,name='delete-blog'),
#         path('delete-img',views.delete_img,name='delete-img'),
#         path('check-box',views.check_box,name='check-box'),
#         path('forget_password',views.forget_password,name='forget_password')

# ]      

urlpatterns = [
        path('',views.admin_login.as_view(),name='admin-login'),
        path('dashboard', views.dashboard.as_view(), name='dashboard'),
        path('Blog', views.blog.as_view(), name='Blog'),
        path('logout',views.logout_admin.as_view(), name='logout'),
        path('create_blog',views.create_blog.as_view(), name='create_blog'),
        path('status',views.status.as_view(), name='status'),
        path('descriptionn',views.description_blog.as_view(), name='descriptionn'),
        path('edit_blog',views.edit_blog.as_view(), name='edit_blog'),
        path('edit_blog_action',views.edit_blog_action.as_view(),name='edit_blog_action'),
        path('delete-blog',views.delete_blog.as_view(),name='delete-blog'),
        path('delete-img',views.delete_img.as_view(),name='delete-img'),
        path('check-box',views.check_box.as_view(),name='check-box'),
        path('forget_password',views.forget_password.as_view(),name='forget_password'),
        path('service',views.service.as_view(),name='service'),
        path('create_service',views.create_service.as_view(),name='create_service'),
        path('edit_service_action',views.edit_service_action.as_view(),name='edit_service_action'),
        path('edit_service',views.edit_service.as_view(),name='edit_service'),
        path('description_service',views.description_service.as_view(),name='description_service'),
        path('delete-service',views.delete_service.as_view(),name='delete-service'),
        path('service_check-box',views.check_service_box.as_view(),name='service_check-box'),
        path('delete_img_service',views.delete_img_service.as_view(),name='delete_img_service')

]        

