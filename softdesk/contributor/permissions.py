from rest_framework.permissions import BasePermission
from rest_framework import permissions

from contributor.models import Contributor
from project.models import Project


CONTRIBUTOR_PERMS = ['GET', 'POST']
CREATOR_PERMS = ['PUT', 'DELETE', 'GET', 'POST']


class IsCreator(BasePermission):

    def has_permission(self, request, view):
        print(view.kwargs)
        project = Project.objects.get(id=view.kwargs['projects__pk'])
        print(project.creator.id == request.user.id)
        if project.creator.id == request.user.id:
            if request.method in CREATOR_PERMS:
                return True


class IsContributor(BasePermission):

    def has_permission(self, request, view):

        contributeurs_project = Contributor.objects.filter(
            project_id__id=view.kwargs['projects__pk'])
        for contributor in contributeurs_project:
            if contributor.contributor_id.id == request.user.id:
                if request.method in CONTRIBUTOR_PERMS:
                    return True
