from django.db.models import Q

from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status

from .serializers import ProjectDetailSerializer, ProjectSerializer
from .models import Project
from .permissions import IsProjectAuthor, IsProjectContributor
from rest_framework.permissions import IsAuthenticated

class MultipleSerializerMixin:

    """ Mixin permet d'afficher les vue en détail ou en liste"""

    detail_serializer_class = None

    def get_serializer_class(self):
        if self.action == 'retrieve' and self.detail_serializer_class is not None:
            return self.detail_serializer_class
        return super().get_serializer_class()


class ProjectViewSet(MultipleSerializerMixin, ModelViewSet):

    """ Le ModelViewSet des projets """

    serializer_class = ProjectSerializer
    detail_serializer_class = ProjectDetailSerializer
    permission_classes = [IsProjectAuthor | IsProjectContributor, IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        if "pk" in self.kwargs:
            return Project.objects.filter(pk=self.kwargs['pk'])
        queryset = Project.objects.filter(Q(creator_id=self.request.user.id))
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
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED, headers=headers)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        data = {"response": "Le projet est supprimé."}
        return Response(data, status=status.HTTP_204_NO_CONTENT)
