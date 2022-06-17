from django.shortcuts import render

from todos.models import TodoItem, TodoList
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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


class TodoListUpdateView(UpdateView):
    model = TodoList
    template_name = "todos/edit.html"
    fields = ["name"]
    success_url = reverse_lazy("list_todos")


class TodoListDeleteView(DeleteView):
    model = TodoList
    template_name = "todos/delete.html"
    success_url = reverse_lazy("list_todos")


# def edit_todos(request, pk):
#     todo = TodoList.objects.filter(pk=pk).get()
#     if request.method == "POST":
#         form = TodoListForm (request.POST, instance=todo)
#     context = {
#         "todos_edit": TodoItem.objects.filter(pk=pk),
#     }
#     return render(request, "todos/edit.html", context)


class TodoItemCreateView(CreateView):
    model = TodoItem
    template_name = "todo_items/new.html"
    fields = ["task", "due_date", "is_completed", "list"]
    success_url = reverse_lazy("show_todolist")
