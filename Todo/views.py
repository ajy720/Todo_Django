from django.shortcuts import render
from .models import Todo

# Create your views here.
def main(request):
    context = {"todos": Todo.objects.all()}

    return render(request, "Todo/main.html", context)
