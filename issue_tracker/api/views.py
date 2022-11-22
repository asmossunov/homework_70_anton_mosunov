from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from tracker.models import Task
from api.serializers import TaskSerializer


class TaskDetailView(APIView):

    def get(self, request, *args, **kwargs):
        task = Task.objects.get(id=kwargs['pk'])
        serializer = TaskSerializer(task)
        return Response(serializer.data)



