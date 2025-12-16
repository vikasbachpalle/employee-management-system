from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('add/', views.add_employee, name='add'),
    path('list/', views.list_employee, name='list'),
    path('update/<int:emp_id>/', views.update_employee, name='update'),
    path('delete/<int:emp_id>/', views.delete_employee, name='delete'),
]
