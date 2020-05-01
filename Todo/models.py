from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=50, verbose_name="제목")
    checked = models.BooleanField(verbose_name="완료 여부")

    created_at = models.DateTimeField(auto_now_add=True ,verbose_name="생성 일시")
    complete_at = models.DateTimeField(auto_now=True, verbose_name="완료 일시")