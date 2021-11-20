from django.urls import path

from todos.views import list_todos, create_todo

urlpatterns = [
    path('', list_todos, name='list todos'),
    path('create/', create_todo, name='create todo'),
]