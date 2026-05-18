from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from users.views import RegisterView, LoginView
from users.password_reset import PasswordResetRequestView, PasswordResetConfirmView
from vehicles.views import VehicleViewSet

router = DefaultRouter()
router.register(r'vehicles', VehicleViewSet, basename='vehicle')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/register/', RegisterView.as_view()),
    path('api/auth/login/', LoginView.as_view()),
    path('api/auth/refresh/', TokenRefreshView.as_view()),
    path('api/auth/password-reset/', PasswordResetRequestView.as_view()),
    path('api/auth/password-reset/confirm/', PasswordResetConfirmView.as_view()),
    path('api/', include(router.urls)),
]