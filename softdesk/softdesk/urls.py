from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_nested import routers

from user.views import SignUpViewSet
from project.views import ProjectViewSet
from issue.views import IssueViewSet
from contributor.views import ContributorViewSet
from comment.views import CommentViewSet


router = routers.SimpleRouter()
router.register('signup', SignUpViewSet, basename='signup')

projects_router = routers.SimpleRouter()
projects_router.register(r"projects/?", ProjectViewSet, basename="projects")

issues_router = routers.NestedSimpleRouter(projects_router, r"projects/?", lookup="projects")
issues_router.register(r"issues/?", IssueViewSet, basename="issues")

contributors_router = routers.NestedSimpleRouter(projects_router, r"projects/?", lookup="projects")
contributors_router.register(r"contributors/?", ContributorViewSet, basename="contributors")

comments_router = routers.NestedSimpleRouter(issues_router, r"issues/?", lookup="issues")
comments_router.register(r"comments/?", CommentViewSet, basename="comments")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('login/', TokenObtainPairView.as_view(), name='obtain_tokens'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='refresh_token'),
    path("", include(projects_router.urls)),
    path("", include(issues_router.urls)),
    path('', include(router.urls))
]
