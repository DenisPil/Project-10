from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from django.db.models import Q

from .models import Contributor
from .serializers import ContributorSerializer


class ContributorViewSet(ModelViewSet):

    """ Le ModelViewSet des contributeurs """

    serializer_class = ContributorSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Contributor.objects.all()
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

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        data = {"response": "L'utilisateur est supprimé."}
        return Response(data, status=status.HTTP_204_NO_CONTENT)
