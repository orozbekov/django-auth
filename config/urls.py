from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view


"""=============Swagger docs============="""

swagger_view = get_schema_view(
    openapi.Info(
        title="Auth API",
        default_version='v1',
        description="auth API"
    ),
    public=True
)
"""======================================"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', swagger_view.with_ui('swagger', cache_timeout=0)),
    path('auth/', include('apps.accounts.urls'))
]
