from django.urls import path
from . import views
from .views import user_login_view, user_logout_view

app_name = 'scholarship_post'

urlpatterns = [
    path('user_registration/', views.user_registration, name='user-registration'),
    path('', views.user_login_view, name='user-login'),
    path('home/', views.home, name='home'),
    path('user_logout_view/', views.user_logout_view, name='user-logout'),
    
    path('scholarships_blog_list/', views.scholarships_blog_list, name='scholarship-blog-list'),
    path('add_scholarships/add/', views.add_scholarship, name='add-scholarship'),
   
    path('delete_scholarship/delete/<int:pk>/', views.delete_scholarship, name='delete-scholarship'),
    path('scholarship_detail/<int:pk>/', views.scholarship_detail, name='scholarship-detail'),
    path('scholarship_update/update/<int:pk>/', views.update_scholarship, name='update-scholarship'),
    path('Contact-us/', views.ContactUsView, name='contact-us'),

]