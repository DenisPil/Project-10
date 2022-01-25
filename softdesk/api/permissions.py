from xml.etree.ElementTree import Comment
from rest_framework.permissions import BasePermission
from rest_framework import permissions
from .models import Project, Issue, Contributor


METHODES_CREATE_READ = [ 'GET', 'POST' ]
METHODES_PUT_DEL = ['GET', 'POST', 'PUT', 'DELETE']

class IsProjectAuthor(BasePermission):
    """Author of project can Create and Read issues"""
    message = "L'utilisateur doit être l'auteur ou le contributeur du projet"

    def has_permission(self, request, view):
        print(view.kwargs)
        index_project = view.kwargs['pk']
        project = Project.objects.get(id=index_project)
        if project.creator.id == request.user.id: # si le user est l'autheur du projet
            if request.method in METHODES_CREATE_READ: # Pour lecture et ecriture
                print("IsProjectAuthor")
                return True


class IsProjectContributor(BasePermission):
    """Contributors of project can Create and Read issues"""
    message = "L'utilisateur doit être l'auteur ou le contributeur du projet"

    def has_permission(self, request, view):
        index_project = view.kwargs['projects_pk']
        contributeurs_project = Contributor.objects.filter(
            project_id__id=index_project)
        for contributor in contributeurs_project:
            if contributor.user_id.id == request.user.id: #
                if request.method in METHODES_CREATE_READ: # Pour lecture et ecriture
                    print("IsProjectContributor")
                    return True
            
        
class IsIssueAuthor(BasePermission):
    """Author of Issue can Update and Delete issues """
    message = "L'utilisateur doit être l'auteur du problème"

    def has_permission(self, request, view):
        print(request.parser_context, "zezeezeezezezeezezezze---------------------------")
        id_issue = view.kwargs['pk']
        issue = Issue.objects.get(id=id_issue)
        print(issue.assignee_user_id.id == request.user.id)
        if issue.assignee_user_id.id == request.user.id: # si l'utilisateur est l'auteur du problème
            if request.method in METHODES_PUT_DEL: # pour MAJ et suppression
                return True

"""class IsProjectAuthor(BasePermission):
    message = "L'utilisateur n'est pas l'auteur ou un conzezeztributeur"

    def has_permission(self, request, view):
        print(view.kwargs,'é"é"é"é"é"')
        index_project = view.kwargs['projects__pk']
        project = Project.objects.get(id=index_project)
        if project.creator.id == request.user.id:
            if request.method in METHODES_CREATE_READ:
                return True
class IsProjectAuthor(BasePermission):
    
    message = "L'utilisateur doit être l'auteur ou le contributeur du projet"

    def has_object_permission(self, request, view, obj):
               
        if obj.creator.id == request.user.id:
            return True
            
class IsProjectContributor(BasePermission):
    message = "L'utilisateur n'est pas  un contributeur"

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
        print(view.kwargs, "ISSUE")
        id_issue = view.kwargs["projects__pk"]
        
        issue = Issue.objects.get(id=id_issue)
        if issue.assignee_user_id.id == request.user.id:
            if request.method in METHODES_PUT_DEL:
                return True

class IsCommentAuthor(BasePermission):
    message = "L'utilisateur n'est pas l'auteur du commentaire"

    def has_permission(self, request, view):
    
        print(view.kwargs['pk'])
        id_issue = view.kwargs['pk']
        issue = Issue.objects.get(id=id_issue)
        if issue.assignee_user_id.id == request.user.id: # si l'utilisateur est l'auteur du problème
            if request.method in METHODES_PUT_DEL: # pour MAJ et suppression
                return True"""