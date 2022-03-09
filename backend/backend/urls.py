"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

# import router
from rest_framework.routers import DefaultRouter

# import views
from users.views import MyObtainTokenPairView, RegisterView, GetUserView
from posts.views import PostAPIViewset, CommentAPIViewset, SubCommentAPIViewset
from groups.views import GroupAPIViewset
# token authentication over json
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# declare routers
router = DefaultRouter()
router.register(r'posts', PostAPIViewset, basename='Posts')
router.register(r'groups', GroupAPIViewset, basename='Groups')
router.register(r'comments', CommentAPIViewset, basename='Comments')
router.register(r'subcomments', SubCommentAPIViewset, basename='SubComments')
router.register(r'user', GetUserView, basename='User')





urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')), # new
    
    # token needed for sessions
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api-auth/', include('rest_framework.urls')),
    
    # login rest api view
    path('api/login/', MyObtainTokenPairView.as_view(), name='login_token_obtain_pair'),
    path('api/login/refresh/', TokenRefreshView.as_view(), name='login_token_refresh'),
    path('api/register/', RegisterView.as_view(), name='auth_register'),
    # path("/create_random_users", createRandomUsers, name="create_random_users"),
    
    # include routers for post groups and comments
    path('api/', include(router.urls)),
    # path('upload/', MemeImageAPIViewset.as_view, name='upload'),

]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

