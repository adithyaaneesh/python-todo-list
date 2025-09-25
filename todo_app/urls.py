from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='home'),
    path('add/',views.add_task, name='add_task'),
    path('complete_task/<int:task_id>/',views.complete_task, name='complete_task'),
    path('update_task/<int:task_id>/',views.update_task, name='update_task'),
    path('delete_task/<int:task_id>/',views.delete_task, name='delete_task'),
]