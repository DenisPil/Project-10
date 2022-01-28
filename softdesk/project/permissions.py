from rest_framework.permissions import BasePermission
from rest_framework import permissions
from contributor.models import Contributor


CONTRIBUTOR_PERMS = ['GET', 'POST']
CREATOR_PERMS = ['PUT', 'DELETE']


class IsProjectAuthor(BasePermission):

    message = "Vous n'avez pas la permission d'effectuer cette action."

    def has_object_permission(self, request, view, obj):
        if obj.creator.id == request.user.id:
            return True


class IsProjectContributor(BasePermission):

    message = "Vous n'avez pas la permission d'effectuer cette action."

    def has_object_permission(self, request, view, obj):
        contributors = Contributor.objects.filter(
            project_id__id=obj.id)
        for contributor in contributors:
            if contributor.contributor_id.id == request.user.id:
                if request.method in CONTRIBUTOR_PERMS:
                    return True
