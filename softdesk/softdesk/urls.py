from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from api import views

router = routers.SimpleRouter()
router.register('project', views.ProjectViewSet, basename='project')
router.register('issue', views.IssueViewSet, basename='issue')
router.register('comment', views.CommentViewSet, basename='comment')
router.register('signup', views.SignUpViewSet, basename='signup')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('',include(router.urls)),

]

"""
    endpoint :  
                http://127.0.0.1:8000/api/issue/?project_id='ID'
                http://127.0.0.1:8000/api/comment/?issue_id='ID'
                
                
                
                
                
                
                
                
                
                
                
                

"""