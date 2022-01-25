
from msilib.schema import Error
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet  # ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.decorators import api_view
from django.db.models import Q
from .models import Project, Issue,  Com, Contributor
from .serializers import  ContributorSerializer, ProjectDetailSerializer, ProjectSerializer, SignupSerializer, CommentSerializer, IssueSerializer, IssueDetailSerializer
from django.contrib.auth.decorators import login_required, permission_required
from .permissions import IsProjectAuthor,  IsIssueAuthor, IsProjectContributor #, IsCommentAuthor, IsProjectContributor 


class MultipleSerializerMixin:
    
    detail_serializer_class = None

    def get_serializer_class(self):
        if self.action == 'retrieve' and self.detail_serializer_class is not None:
            return self.detail_serializer_class
        return super().get_serializer_class()


class ProjectViewSet(MultipleSerializerMixin, ModelViewSet):
    
    serializer_class = ProjectSerializer
    detail_serializer_class = ProjectDetailSerializer
    permission_classes = [IsProjectAuthor]

    def get_queryset(self,*args, **kwargs):
        """print(self.request.GET.get("id")rr)
        gg = Contributor.objects.filter(contributor_id=self.request.user.id)
        for i in gg:
            print(i.role, i.contributor_id.id)"""
        queryset = Project.objects.filter(Q(creator_id=self.request.user.id))# |
                                          #Q(contributor=self.request.user.id))
        """contributor = self.request.GET.get('contributor')
        if contributor:
            queryset = queryset.filter(contributor=contributor)"""
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class IssueViewSet(MultipleSerializerMixin, ModelViewSet):
    
    serializer_class = IssueSerializer
    detail_serializer_class = IssueDetailSerializer
    permission_classes = [IsIssueAuthor or IsProjectAuthor or IsProjectContributor]
    
    def get_queryset(self,*args, **kwargs):
        queryset = Issue.objects.all()
        project_id = self.request.parser_context['kwargs']['projects__pk']
        if project_id:
            queryset = queryset.filter(project_id=project_id)
            print(queryset)
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class CommentViewSet(ModelViewSet):

    serializer_class = CommentSerializer
    #permission_classes = [IsAuthenticated, IsCommentAuthor]
    def get_queryset(self):
        queryset = Com.objects.all()
        issue_id = self.request.GET.get('issue_id')
        if issue_id:
            queryset = queryset.filter(issue_id=issue_id)
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class SignUpViewSet(ModelViewSet):

    serializer_class = SignupSerializer

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


class ContributorViewSet(ModelViewSet):

    serializer_class = ContributorSerializer
    #permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Contributor.objects.all()
        project_id = self.request.parser_context['kwargs']['projects__pk']
        print(project_id)
        if project_id:
            queryset = queryset.filter(project_id=project_id)
            print(queryset)
        return queryset

    def create(self, request, *args, **kwargs):
        project = Project.objects.filter(Q(id=request.data['project_id']))
        project_creator = Project.objects.filter(Q(creator=request.data['contributor_id'])| Q(id=request.data['project_id']))
        #contributors = project[0].contributor.all()
        """if  int(project_creator[0].creator.id) == int(request.data['contributor_id']) and request.data['role'] != 'CREATOR':
            error =("L'utilisateur est le créateur du projet")
            return Response(error,status=status.HTTP_400_BAD_REQUEST)
        for contributor in contributors:
            if int(request.data['contributor_id']) == contributor.id:
                error =("L'utilisateur est déja dans le projet")
                return Response(error,status=status.HTTP_400_BAD_REQUEST)"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
