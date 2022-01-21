
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet  # ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.decorators import api_view
from django.db.models import Q
from .models import Project, Issue,  Com
from .serializers import  ProjectSerializer, SignupSerializer, CommentSerializer, IssueSerializer


class ProjectViewSet(ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Project.objects.filter(Q(creator_id=self.request.user.id) |
                                          Q(contributor=self.request.user.id))
        return queryset


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


class SignUpViewSet(ModelViewSet):
    serializer_class = SignupSerializer
    # @api_view(['POST'])
    def create(self, request):
        serializer = SignupSerializer(data=request.data)
        data = {}
        if serializer.is_valid(request):
            account = serializer.save()
            data['response'] = "Successfully registered a new user"
            data['email'] = account.email
            data['username'] = account.username
        else:
            data = serializer.error
        return Response(data)