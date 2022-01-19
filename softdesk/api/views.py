
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet  # ReadOnlyModelViewSet
from rest_framework import status

from .models import Issue, Project, Com
from .serializers import CommentSerializer, ProjectSerializer, IssueSerializer, SignupSerializer


class ProjectViewSet(ModelViewSet):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return Project.objects.all()


class IssueViewSet(ModelViewSet):
    serializer_class = IssueSerializer

    def get_queryset(self):
        queryset = Issue.objects.all()
        project_id = self.request.GET.get('project_id')
        if project_id:
            queryset = queryset.filter(project_id=project_id)
        return queryset


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        queryset = Com.objects.all()
        issue_id = self.request.GET.get('issue_id')
        if issue_id:
            queryset = queryset.filter(issue_id=issue_id)
        return queryset


def registration_view(request):
    if request.method =='POST':
        serializer = SignupSerializer
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = "Successfully registered a new user"
            data['email'] = account.email
            data['username'] = account.username
        else:
            data = serializer.error
        return Response(data)