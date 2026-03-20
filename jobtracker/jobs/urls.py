from django.urls import path
from .views import job_list, add_job,edit_job,delete_job
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', job_list, name='job_list'),
    path('add/', add_job, name='add_job'),
path('edit/<int:id>/', edit_job, name='edit_job'),
path('delete/<int:id>/', delete_job, name='delete_job'),
    path('password_reset/',
         auth_views.PasswordResetView.as_view(
             template_name='registration/password_reset.html'
         ),
         name='password_reset'),

    path('password_reset_done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='registration/password_reset_done.html'
         ),
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='registration/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),

    path('reset_done/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='registration/password_reset_complete.html'
         ),
         name='password_reset_complete'),
]

