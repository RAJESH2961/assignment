from rest_framework import serializers
from .models import Client, Project

class ClientSerializer(serializers.ModelSerializer):
    projects = serializers.SerializerMethodField()

    class Meta:
        model = Client
        fields = '__all__'

    def get_projects(self, obj):
        return [{"id": proj.id, "name": proj.project_name} for proj in obj.projects.all()]


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
