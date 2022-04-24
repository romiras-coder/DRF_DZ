from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('mainapp.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api-auth-token/', views.obtain_auth_token),
    path('api-auth-token/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api-auth-token/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
