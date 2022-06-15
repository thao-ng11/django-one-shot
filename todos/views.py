from django.shortcuts import render

from todos.models import TodoItem, TodoList


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
