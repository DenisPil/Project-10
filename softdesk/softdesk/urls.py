from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_nested import routers
from api import views
from django.conf import settings





router = routers.SimpleRouter()
projects_router = routers.SimpleRouter(trailing_slash=False)
# projects_router.register('project', views.ProjectViewSet, basename='project')
projects_router.register(r"project/?", views.ProjectViewSet, basename="project")


issues_router = routers.NestedSimpleRouter(projects_router, r"project/?", lookup="project", trailing_slash=False)
issues_router.register(r"issues/?", views.IssueViewSet, basename="issues")
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    path('api/token/', TokenObtainPairView.as_view(), name='obtain_tokens'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='refresh_token'),
    path("", include(projects_router.urls)),
	path("", include(issues_router.urls)),
    path('', include(router.urls))


]




"""
    endpoint :  
                http://127.0.0.1:8000/api/issue/?project_id='ID'
                http://127.0.0.1:8000/api/comment/?issue_id='ID'
                
                
                
                
                
                
                
                
                
                
                
                

"""
