from django.urls import path
from . import views

urlpatterns = [
    #path('email-list/', views.email_list_view, name='email_list'),
    #path('start-email-import/', views.start_email_import, name='start_email_import'),
    path('', views.add_email_account, name='add_email_account'),
]