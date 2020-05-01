from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import Todo
from .form import TodoForm
import pdb


def main(request):
    context = {"todos": Todo.objects.all()}

    return render(request, "Todo/main.html", context)


@require_POST
def update(request):
    form = TodoForm(request.POST)

    if form.is_valid():
        form.save()

    return redirect("Todo:main")
