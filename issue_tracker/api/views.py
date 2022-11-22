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


class TaskUpdateView(APIView):

    def put(self, request, pk):
        task = Task.objects.get(pk=pk)
        serializer = TaskSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskDeleteView(APIView):

    def delete(self, request, pk, format=None):
        task = Task.objects.get(pk=pk)
        task.delete()
        return Response(data={"id": task.id})
