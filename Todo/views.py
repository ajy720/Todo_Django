from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import Todo
from .form import TodoForm
import pdb


def main(request):
    context = {"todos": Todo.objects.all()}

    return render(request, "Todo/main.html", context)


@require_POST
def create(request):
    form = TodoForm(request.POST)

    if form.is_valid():
        form.save()

    return redirect("Todo:main")


@require_POST
def check(request):
    todo = Todo.objects.get(id=request.POST.get("id"))

    todo.checked ^= True
    todo.save()

    return redirect("Todo:main")


@require_POST
def update(request):
    todo = Todo.objects.get(id=request.POST.get("id"))

    todo.title = request.POST.get("title")
    todo.save()

    return redirect("Todo:main")


@require_POST
def delete(request):
    todo = Todo.objects.get(id=request.POST.get("id"))

    todo.delete()
    return redirect("Todo:main")
