from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status

from .serializers import IssueSerializer, IssueDetailSerializer
from .models import Issue
from .permissions import IsIssueCreator, IsCreator, IsContributor


class MultipleSerializerMixin:

    """ Mixin permet d'afficher les vues en détail ou en liste"""

    detail_serializer_class = None

    def get_serializer_class(self):
        if self.action == 'retrieve' and self.detail_serializer_class is not None:
            return self.detail_serializer_class
        return super().get_serializer_class()


class IssueViewSet(MultipleSerializerMixin, ModelViewSet):

    """ Le ModelViewSet des problèmes """

    serializer_class = IssueSerializer
    detail_serializer_class = IssueDetailSerializer
    permission_classes = [IsIssueCreator | IsCreator | IsContributor]

    def get_queryset(self, *args, **kwargs):
        queryset = Issue.objects.all()
        project_id = self.request.parser_context['kwargs']['projects__pk']
        if project_id:
            queryset = queryset.filter(project_id=project_id)
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
        data = {"response": "Le problème est supprimé."}
        return Response(data, status=status.HTTP_204_NO_CONTENT)
