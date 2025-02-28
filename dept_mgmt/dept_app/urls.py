from django.urls import path
from dept_app import views

urlpatterns = [
    path('',views.index,name='home'),
    path('add_dept',views.add_dept,name='add_dept'),
    path('edit_dept', views.edit_dept, name='edit_dept'),
    path('update/<int:id>/', views.update_department, name='update_department'),
    path('delete/<int:id>/', views.delete_dept, name='delete_dept'),
    
]
