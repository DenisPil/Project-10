from genericpath import exists

from rest_framework.permissions import BasePermission
from rest_framework import permissions
from .models import Com, Project, Issue, Contributor
from rest_framework.response import Response
from rest_framework import status

CONTRIBUTOR_PERMS = [ 'GET', 'POST' ]
CREATOR_PERMS = ['PUT', 'DELETE']


class IsProjectAuthor(BasePermission):
    
    message = "Vous n'avez pas la permission d'effectuer cette action."

    def has_object_permission(self, request, view, obj):
               
        if obj.creator.id == request.user.id:
            print('CREATOR')
            return True


class IsProjectContributor(BasePermission):

    message = "Vous n'avez pas la permission d'effectuer cette action."

    def has_object_permission(self, request, view, obj):
        index_project = obj.id
        contributors_in_project = Contributor.objects.filter(
            project_id__id=index_project)
        for contributor in contributors_in_project:
            if contributor.contributor_id.id == request.user.id:
                if request.method in CONTRIBUTOR_PERMS:
                    return True


class IsIssueAuthor(BasePermission):
    
    message = "Vous n'avez pas la permission d'effectuer cette action."
    
    def has_object_permission(self, request, view, obj):
        issue = Issue.objects.get(id=obj.id)
        print(issue.creator.id == request.user.id,issue.creator.id, request.user.id)
        if issue.creator.id == request.user.id:
            if request.method in CREATOR_PERMS: 
                return True
        if issue.creator.id != request.user.id:
            if request.method in CONTRIBUTOR_PERMS: 
                return True

class IsCommentAuthor(BasePermission):
    
    message = "Vous n'avez pas la permission d'effectuer cette action."
    
    def has_object_permission(self, request, view, obj):
        print(obj.id)
        com = Com.objects.get(id=obj.id)
        print(com.creator.id == request.user.id,com.creator.id, request.user.id)
        if com.creator.id == request.user.id:
            if request.method in CREATOR_PERMS: 
                return True
        if com.creator.id != request.user.id:
            if request.method in CONTRIBUTOR_PERMS: 
                return True























"""class IsProjectAuthor(BasePermission):

    message = ""

    def has_permission(self, request, view):
        index_project = view.kwargs['projects__pk']
        project = Project.objects.get(id=index_project)
        if project.creator.id == request.user.id:
            if request.method in CONTRIBUTOR_PERMS:
                return True"""