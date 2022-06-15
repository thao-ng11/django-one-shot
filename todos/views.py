from django.shortcuts import render

from todos.models import TodoItem, TodoList
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


# Create your views here.


def list_todos(request):
    context = {"todos_list": TodoList.objects.all()}
    return render(
        request=request, template_name="todos/list.html", context=context
    )


def detail_todos(request, pk):
    context = {
        "todos_detail": TodoItem.objects.filter(pk=pk),
    }
    return render(request, "todos/detail.html", context)


class TodoListCreateView(CreateView):
    model = TodoList
    template_name = "todos/new.html"
    fields = ["name"]
    success_url = reverse_lazy("list_todos")
