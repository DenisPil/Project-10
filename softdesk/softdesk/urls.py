from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from api import views

router = routers.SimpleRouter()
router.register('project', views.ProjectViewSet, basename='project')
router.register('issue', views.IssueViewSet, basename='issue')
router.register('comment', views.CommentViewSet, basename='comment')
router.register('signup', views.SignUpViewSet, basename='signup')
router.register('contributor', views.ContributorViewSet, basename='contributor')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('',include(router.urls)),    
    path('api/token/', TokenObtainPairView.as_view(), name='obtain_tokens'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='refresh_token'),

]

"""
    endpoint :  
                http://127.0.0.1:8000/api/issue/?project_id='ID'
                http://127.0.0.1:8000/api/comment/?issue_id='ID'
                
                
                
                
                
                
                
                
                
                
                
                

"""