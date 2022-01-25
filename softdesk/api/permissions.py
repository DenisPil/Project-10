from rest_framework.permissions import BasePermission
from rest_framework import permissions
from .models import Project, Issue, Contributor


METHODES_CREATE_READ = [ 'GET', 'POST' ]
METHODES_PUT_DEL = [ 'PUT', 'DELETE']


class IsProjectAuthor(BasePermission):
    message = "L'utilisateur n'est pas l'auteur ou un contributeur"

    def has_permission(self, request, view):
        index_project = view.kwargs['projects__pk']
        project = Project.objects.get(id=index_project)
        if project.creator.id == request.user.id:
            if request.method in METHODES_CREATE_READ:
                print("l'utilisateur est l'author du projet")
                return True


class IsProjectContributor(BasePermission):
    message = "L'utilisateur n'est pas l'auteur ou un contributeur"

    def has_permission(self, request, view):
        index_project = view.kwargs['projects__pk']
        contributeurs_project = Contributor.objects.filter(
            project_id__id=index_project)
        for contributor in contributeurs_project:
            if contributor.user_id.id == request.user.id:
                if request.method in METHODES_CREATE_READ:
                    return True
            
        
class IsIssueAuthor(BasePermission):
    message = "L'utilisateur n'est pas l'auteur du problème"

    def has_permission(self, request, view):
        
        id_issue = view.kwargs['pk']
        issue = Issue.objects.get(id=id_issue)
        if issue.assignee_user_id.id == request.user.id:
            if request.method in METHODES_PUT_DEL:
                return True