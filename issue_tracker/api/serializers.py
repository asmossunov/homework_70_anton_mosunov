from django.contrib.auth.models import User
from rest_framework import serializers
from tracker.models import Task, Type, Status

from tracker.models import Project


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ('id', 'type_name', 'created_at', 'updated_at')
        read_only_fields = ('id', 'type_name', 'created_at', 'updated_at')



class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ('id', 'status_name', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')



class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'start_date', 'end_date', 'project_name', 'project_description', 'is_deleted',
                  'created_at', 'changed_at', 'users')
        read_only_fields = ('id',  'created_at', 'updated_at', 'is_deleted')


class TaskSerializer(serializers.ModelSerializer):
    project = ProjectSerializer(read_only=True)
    status = StatusSerializer(read_only=True)
    types = TypeSerializer(read_only=True)


    class Meta:
        model = Task
        fields = ('id', 'text', 'project', 'types', 'description', 'is_deleted', 'created_at', 'changed_at', 'status')
        read_only_fields = ('id', 'created_at', 'updated_at')

