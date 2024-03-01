from django.urls import path
from . import views
urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('detail/<int:id>', views.task_detail, name='task_details'),
    path('creat/', views.creat_task, name='task_creat'),
    path('update/<int:id>', views.edit_task, name='task_update'),
    path('delete/<int:id>', views.delete_task, name='task_delete')
]
