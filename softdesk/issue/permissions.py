from rest_framework.permissions import BasePermission
from rest_framework import permissions
from contributor.models import Contributor
from issue.models import Issue
from project.models import Project


CONTRIBUTOR_PERMS = ['GET', 'POST']
CREATOR_PERMS = ['PUT', 'DELETE']


class IsCreator(BasePermission):

    def has_permission(self, request, view):
        project = Project.objects.get(id=view.kwargs['projects__pk'])
        if project.creator.id == request.user.id:
            if request.method in CONTRIBUTOR_PERMS:
                return True


class IsContributor(BasePermission):

    def has_permission(self, request, view):
        contributeurs_project = Contributor.objects.filter(
            project_id__id=view.kwargs['projects__pk'])
        for contributor in contributeurs_project:
            if contributor.contributor_id.id == request.user.id:
                if request.method in CONTRIBUTOR_PERMS:
                    return True


class IsIssueCreator(BasePermission):

    def has_permission(self, request, view):
        if 'pk' in view.kwargs:
            issue = Issue.objects.get(id=view.kwargs['pk'])
            if issue.assignee_user_id.id == request.user.id:
                if request.method in CREATOR_PERMS:
                    return True
