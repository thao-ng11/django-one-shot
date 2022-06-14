from django.shortcuts import render

from todos.models import TodoList


# Create your views here.


def list_todos(request):
    context = {"todos_list": TodoList.objects.all()}
    return render(request, "todos/list.html", context)


def detail_todos(request):
    pass
