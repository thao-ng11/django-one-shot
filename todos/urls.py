from django.urls import path

from todos.views import list_todos

urlpatterns = [
    path("", list_todos, name="list_todos"),
]
