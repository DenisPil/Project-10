from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status

from django.db.models import Q

from .models import Com
from .serializers import CommentSerializer
from .permissions import IsCreator, IsContributor, IsCommentCreator

class CommentViewSet(ModelViewSet):

    """ Le ModelViewSet des commentaires """

    serializer_class = CommentSerializer
    permission_classes = [IsCreator | IsContributor |IsCommentCreator]

    def get_queryset(self):
        queryset = Com.objects.all()
        print(self.request.parser_context)
        issue_id = self.request.parser_context['kwargs']['issues__pk']
        print(issue_id)
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
        data = {"response": "Le commentaire est supprimé."}
        return Response(data, status=status.HTTP_204_NO_CONTENT)
