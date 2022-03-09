from django.urls import path

from TodoApp.Todo.views import MyTodosView, todo_action_view, delete_todo, DeleteTodoView

urlpatterns = [
    path('', MyTodosView.as_view(), name='my todos'),
    path('action/<int:pk>', todo_action_view, name='action todo'),
    path('delete/<int:pk>', delete_todo, name='delete todo'),
    path('delete/todo/<int:pk>', DeleteTodoView.as_view(), name='delete view'),
]
