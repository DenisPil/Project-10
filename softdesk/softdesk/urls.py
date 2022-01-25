from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_nested import routers
from api import views
from django.conf import settings





router = routers.SimpleRouter()
router.register('signup', views.SignUpViewSet, basename='signup')
projects_router = routers.SimpleRouter()
# projects_router.register('project', views.ProjectViewSet, basename='project')
projects_router.register(r"projects/?", views.ProjectViewSet, basename="projects")


issues_router = routers.NestedSimpleRouter(projects_router, r"projects/?", lookup="projects")
issues_router.register(r"issues/?", views.IssueViewSet, basename="issues")

contributors_router = routers.NestedSimpleRouter(projects_router, r"projects/?", lookup="projects")
contributors_router.register(r"contributors/?", views.ContributorViewSet, basename="contributors")

comments_router = routers.NestedSimpleRouter(issues_router, r"issues/?", lookup="issues")
comments_router.register(r"comments/?", views.IssueViewSet, basename="comments")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    path('api/token/', TokenObtainPairView.as_view(), name='obtain_tokens'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='refresh_token'),
    path("", include(projects_router.urls)),
	path("", include(issues_router.urls)),
    path('', include(router.urls))


]

"""# création du routeur
router = routers.SimpleRouter()
# déclaration de project afin de générer l'URL correspondante
projects_router = routers.SimpleRouter(trailing_slash=False)
projects_router.register(r"projects/?", ProjectViewset, basename="projects")

users_router = routers.NestedSimpleRouter(projects_router, r"projects/?", lookup="projects", trailing_slash=False)
users_router.register(r"users/?", ContributorViewset, basename="users")

issues_router = routers.NestedSimpleRouter(projects_router, r"projects/?", lookup="projects", trailing_slash=False)
issues_router.register(r"issues/?", IssueViewset, basename="issues")
comments_router = routers.NestedSimpleRouter(issues_router, r"issues/?", lookup="issues", trailing_slash=False)
comments_router.register(r"comments/?", CommentViewset, basename="comments")

urlpatterns = [

	path("", include(comments_router.urls)),

	path('', include(router.urls)), # urls du router pour rendre les urls disponibles
	#path('', include('user.urls')),
]



endpoint :  
                http://127.0.0.1:8000/api/issue/?project_id='ID'
                http://127.0.0.1:8000/api/comment/?issue_id='ID'
                
                
                
                
                
                
                
                
                
                
                
                

"""
