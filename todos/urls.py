from django.urls import path

from todos.views import (
    TodoListCreateView,
    # TodoListUpdateView,
    detail_todos,
    list_todos,
    TodoListUpdateView,
    TodoListDeleteView,
    TodoItemCreateView,
    TodoItemUpdateView,
)

urlpatterns = [
    path("", list_todos, name="list_todos"),
    path("<int:pk>/", detail_todos, name="show_todolist"),
    path("create/", TodoListCreateView.as_view(), name="create_todolist"),
    # path("<int:pk>/edit", edit_todos, name="update_todolist"),
    path("<int:pk>/edit", TodoListUpdateView.as_view(), name="update_todolist"),
    path(
        "<int:pk>/delete", TodoListDeleteView.as_view(), name="delete_todolist"
    ),
    path("items/create/", TodoItemCreateView.as_view(), name="create_todoitem"),
    path(
        "items/<int:pk>/edit/",
        TodoItemUpdateView.as_view(),
        name="update_todoitem",
    ),
]
