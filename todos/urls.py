from django.urls import path

from todos.views import TodoListView

urlpatterns = [
    path("", TodoListView.as_view(), name="to_dos_list"),
]
