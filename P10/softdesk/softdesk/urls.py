from django.contrib import admin
from django.urls import path, include
from rest_framework_nested import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from authentication.views import RegisterViewSet
from issues.views import IssueViewSet
from comments.views import CommentViewSet
from projects.views import ProjectViewSet
from contributors.views import ContributorsViewSet


router = routers.SimpleRouter()
router.register(r'projects', ProjectViewSet, basename='projects')

router_issues = routers.NestedSimpleRouter(router, r'projects', lookup='project_id')
router_issues.register(r'issues', IssueViewSet, basename='issues')

router_comments = routers.NestedSimpleRouter(router_issues, r'issues', lookup='issue_id')
router_comments.register(r'comments', CommentViewSet, basename='comments')

router_contributors = routers.NestedSimpleRouter(router, r'projects', lookup='project_id')
router_contributors.register(r'contributors', ContributorsViewSet, basename='contributors')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/signup/', RegisterViewSet.as_view(), name='register'),
    path('api/', include(router_issues.urls)),
    path('api/', include(router_comments.urls)),
    path('api/', include(router.urls)),
    path('api/', include(router_contributors.urls)),
]
