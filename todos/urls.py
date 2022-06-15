from django.urls import path

from todos.views import TodoListCreateView, detail_todos, list_todos

urlpatterns = [
    path("", list_todos, name="list_todos"),
    path("<int:pk>/", detail_todos, name="show_todolist"),
    path("create/", TodoListCreateView.as_view(), name="create_todolist"),
]
