from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["title", "checked"]
        labels = {"title": "할 일", "checked": "완료 여부"}
