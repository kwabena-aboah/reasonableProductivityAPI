from django.shortcuts import render
from rest_framework import viewsets
from . serializer import TaskSerializer
from . models import Task


def home(request):
    return render(request, 'index.html')


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
