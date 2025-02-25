from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Client, Project
from .serializers import ClientSerializer, ProjectSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated]


    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    @action(detail=False, methods=['get'])
    def assigned_to_user(self, request):
        projects = Project.objects.filter(users=request.user)
        serializer = self.get_serializer(projects, many=True)
        return Response(serializer.data)
