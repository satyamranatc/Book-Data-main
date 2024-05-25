from django.urls import path
from . import views

urlpatterns = [
    path('', views.AdminPage, name='MyAdminPage'),
    path('Submit_Book/', views.SubmitBook, name='SubmitBook'),
]
